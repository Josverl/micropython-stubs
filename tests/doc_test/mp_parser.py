import __future__

import re

from doctest import DocTestParser as StdDocTestParser

from sybil import Example, Region
from sybil.typing import Evaluator

from mp_runner import run_micropython_code, reset_micropython_mcu
from mp_evaluator import MicroPythonEvaluator, MicroPythonDocTestEvaluator


class MicroPythonDocTestParser:
    """
    Custom doctest parser that runs doctests on MicroPython MCU
    """

    def __init__(self):
        self.evaluator = MicroPythonDocTestEvaluator()

    def __call__(self, document):
        """Parse document and yield regions for doctest examples"""

        # Use standard doctest parser
        parser = StdDocTestParser()

        lines = document.text.split("\n")
        i = 0

        # Find all doctest directive regions to avoid conflicts
        doctest_directive_regions = []
        in_doctest_directive = False
        directive_start = None

        for line_idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped == ".. doctest::":
                in_doctest_directive = True
                directive_start = line_idx
            elif in_doctest_directive and line and not line.startswith(" ") and not line.startswith("\t"):
                # End of doctest directive block
                if directive_start is not None:
                    doctest_directive_regions.append((directive_start, line_idx))
                in_doctest_directive = False
                directive_start = None

        # Handle case where doctest directive goes to end of file
        if in_doctest_directive and directive_start is not None:
            doctest_directive_regions.append((directive_start, len(lines)))

        while i < len(lines):
            line = lines[i]

            # Check if we're inside a doctest directive
            inside_directive = any(start <= i < end for start, end in doctest_directive_regions)
            if inside_directive:
                i += 1
                continue

            # Look for the start of a doctest block (>>> line)
            if line.strip().startswith(">>> "):
                start_line = i
                doctest_lines = []

                # Collect the doctest block
                while i < len(lines):
                    current_line = lines[i]
                    stripped = current_line.strip()

                    # Check if we're entering a doctest directive region
                    inside_directive = any(start <= i < end for start, end in doctest_directive_regions)
                    if inside_directive:
                        break

                    if stripped.startswith(">>> ") or stripped.startswith("... "):
                        doctest_lines.append(current_line)
                        i += 1
                    elif not stripped:  # Empty line
                        # Check if next non-empty line is expected output or another construct
                        peek_idx = i + 1
                        while peek_idx < len(lines) and not lines[peek_idx].strip():
                            peek_idx += 1

                        if peek_idx < len(lines):
                            peek_line = lines[peek_idx].strip()
                            # If it's another doctest or RST directive, stop here
                            if peek_line.startswith(">>> ") or peek_line.startswith(".. "):
                                break
                            # Otherwise, include expected output
                            else:
                                # Include the empty line and continue to expected output
                                doctest_lines.append(current_line)
                                i += 1
                        else:
                            break
                    elif not (stripped.startswith(">>>") or stripped.startswith(".. ")):
                        # This is expected output, include it
                        doctest_lines.append(current_line)
                        i += 1
                    else:
                        # Hit another construct, stop
                        break

                # Process the collected doctest block
                doctest_text = "\n".join(doctest_lines)
                examples = parser.get_examples(doctest_text)

                if examples:
                    # Calculate character positions
                    start_pos = sum(len(lines[j]) + 1 for j in range(start_line))  # +1 for newline
                    end_pos = start_pos + len(doctest_text)

                    yield Region(start=start_pos, end=end_pos, parsed=examples, evaluator=self.evaluator)
            else:
                i += 1


class MicroPythonSkipper:
    """
    MCU-aware version of Sybil's Skipper that evaluates conditions on MicroPython MCU
    """

    def __init__(self, directive: str) -> None:
        self.document_state = {}
        self.directive = directive

    def state_for(self, example):
        document = example.document
        if document not in self.document_state:
            from sybil.evaluators.skip import SkipState

            self.document_state[document] = SkipState()
        return self.document_state[example.document]

    def install(self, example, state, reason):
        document = example.document
        document.push_evaluator(self)
        if reason:
            reason = reason.lstrip()
            if reason.startswith("if"):
                condition = reason[2:].strip()
                # Evaluate condition on MCU instead of host
                should_skip = self._evaluate_condition_on_mcu(condition)
                if should_skip:
                    from unittest import SkipTest

                    state.exception = SkipTest("MCU condition evaluated to True")
                else:
                    state.active = False
            else:
                # Handle quoted reasons (non-conditional) - just skip with the quoted reason
                from unittest import SkipTest

                state.exception = SkipTest(reason.strip('"'))
        else:
            # Simple skip directive without reason - always skip
            from unittest import SkipTest

            state.exception = SkipTest("Skipped by directive")

    def remove(self, example):
        document = example.document
        document.pop_evaluator(self)
        del self.document_state[document]

    def evaluate_skip_example(self, example):
        state = self.state_for(example)
        directive = self.directive
        action, reason = example.parsed

        if action not in ("start", "next", "end"):
            raise ValueError("Bad skip action: " + action)
        if state.last_action is None and action not in ("start", "next"):
            raise ValueError(f"'{directive}: {action}' must follow '{directive}: start'")
        elif state.last_action and action != "end":
            raise ValueError(f"'{directive}: {action}' cannot follow '{directive}: {state.last_action}'")

        state.last_action = action

        if action == "start":
            self.install(example, state, reason)
        elif action == "next":
            self.install(example, state, reason)
            state.remove = True
        elif action == "end":
            self.remove(example)
            if reason:
                raise ValueError("Cannot have condition on 'skip: end'")

    def evaluate_other_example(self, example):
        state = self.state_for(example)
        if state.remove:
            self.remove(example)
        if not state.active:
            from sybil.example import NotEvaluated

            raise NotEvaluated()
        if state.exception is not None:
            raise state.exception

    def __call__(self, example):
        if example.region.evaluator is self:
            self.evaluate_skip_example(example)
        else:
            self.evaluate_other_example(example)

    def _evaluate_condition_on_mcu(self, condition: str) -> bool:
        """Evaluate a condition on the MicroPython MCU and return True if should skip"""
        try:
            # Create Python code that evaluates the condition and returns the result
            test_code = f"""
try:
    result = {condition}
    print("SKIP_CONDITION_RESULT:", result)
except Exception as e:
    print("SKIP_CONDITION_ERROR:", str(e))
"""
            output = run_micropython_code(test_code)
            print(f"MCU Skip evaluation output: {output.strip()}")

            # Parse the output
            for line in output.split("\n"):
                if line.startswith("SKIP_CONDITION_RESULT:"):
                    result_str = line.split("SKIP_CONDITION_RESULT:", 1)[1].strip()
                    # Convert string representation back to boolean
                    result = result_str.lower() == "true"
                    print(f"Skip condition '{condition}' evaluated to: {result}")
                    return result
                elif line.startswith("SKIP_CONDITION_ERROR:"):
                    # If there's an error, don't skip (default behavior)
                    print(f"Skip condition error: {line}")
                    return False

            return False  # Default: don't skip if we can't determine the result

        except Exception as e:
            print(f"Error evaluating skip condition on MCU: {e}")
            return False  # Default: don't skip on error


class MicroPythonSkipParser:
    """
    MCU-aware skip parser that subclasses the original SkipParser behavior
    but evaluates conditions on the MicroPython MCU
    """

    def __init__(self):
        from sybil.parsers.rest import SkipParser

        # Create a standard SkipParser and copy its behavior
        self._standard_parser = SkipParser()
        # But use our MCU-aware skipper
        self.skipper = MicroPythonSkipper("skip")
        # Copy the lexers from the standard parser
        self.lexers = self._standard_parser.lexers
        self.directive = "skip"

    def __call__(self, document):
        """Parse document using standard SkipParser logic but with MCU evaluation"""
        for lexed in self.lexers(document):
            arguments = lexed.lexemes["arguments"]
            if arguments is None:
                raise ValueError(f"missing arguments to {self.directive}")

            from sybil.parsers.abstract.skip import SKIP_ARGUMENTS_PATTERN

            match = SKIP_ARGUMENTS_PATTERN.match(arguments)
            if match is None:
                raise ValueError(f"malformed arguments to {self.directive}: {arguments!r}")

            yield Region(lexed.start, lexed.end, match.groups(), self.skipper)


class MicroPythonClearNamespaceParser:
    """
    Parser for clear-namespace directives that resets the MicroPython MCU
    """

    def __call__(self, document):
        """Parse document and yield regions for clear-namespace directives"""
        # Look for clear-namespace directive (with or without ::)
        pattern = r"^(?P<indent> *)\.\.[ \t]+clear-namespace[ \t]*(?:::)?[ \t]*$"

        for match in re.finditer(pattern, document.text, re.MULTILINE):
            yield Region(
                start=match.start(),
                end=match.end(),
                parsed=None,  # No parsing needed
                evaluator=self._clear_namespace_evaluator,
            )

    def _clear_namespace_evaluator(self, example: Example) -> None:
        """Reset the MicroPython MCU to clear the namespace"""
        reset_micropython_mcu()
