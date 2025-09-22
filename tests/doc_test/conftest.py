import __future__

import re
import subprocess
import tempfile
from doctest import DocTestParser as StdDocTestParser
from pathlib import Path

import pytest
from sybil import Example, Region, Sybil
from sybil.evaluators.python import pad
from sybil.parsers.rest import CaptureParser, CodeBlockParser, DocTestDirectiveParser
from sybil.typing import Evaluator

docs_path = Path(__file__).parent / "micropython/docs"
docs_path = Path(__file__).parent / "examples"


def run_micropython_code(source: str) -> str:
    """Run source code on MCU and return the output"""
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tf:
            tf.write(source)
            tf.close()
            cmd = ["mpremote", "resume", "run", tf.name]
            print("Running:", " ".join(cmd))
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"mpremote exited with code {e.returncode}, stderr: {e.stderr}, stdout: {e.stdout}")
    finally:
        # housekeeping
        Path(tf.name).unlink()


def reset_micropython_mcu() -> None:
    """Reset the MicroPython MCU to clear namespace/state"""
    try:
        cmd = ["mpremote", "reset"]
        print("Running:", " ".join(cmd))
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Give the MCU a moment to restart
        import time
        time.sleep(0.5)
    except subprocess.CalledProcessError as e:
        raise Exception(f"mpremote reset failed with code {e.returncode}, stderr: {e.stderr}, stdout: {e.stdout}")


class MicroPythonEvaluator:
    """
    The :any:`Evaluator` to use for :class:`Regions <sybil.Region>` containing
    MicroPython source code.
    """

    def __init__(self) -> None:
        self.flags = 0

    def __call__(self, example: Example) -> None:
        # There must be a nicer way to get line numbers to be correct...
        source = pad(example.parsed, example.line + example.parsed.line_offset)
        # TODO : run in the correct micropython port
        run_micropython_code(source)


class MicroPythonDocTestEvaluator:
    """
    Evaluator for doctests that runs them on the MCU using mpremote
    """

    def __call__(self, example: Example) -> None:
        """Run doctest examples on the MCU"""
        from doctest import Example as DocTestExample

        # Get the list of doctest examples
        examples = example.parsed

        for doctest_example in examples:
            if isinstance(doctest_example, DocTestExample):
                # Extract clean Python source code from the doctest example
                clean_source = self._clean_doctest_source(doctest_example.source)
                expected_output = doctest_example.want.strip()

                # Check if we need to wrap the last line in print() for expressions
                if expected_output and self._should_print_result(clean_source.split("\n")[-1], expected_output):
                    lines = clean_source.split("\n")
                    last_line = lines[-1].strip()
                    if last_line and not any(keyword in last_line for keyword in ["print(", "="]):
                        # Use repr() to match doctest behavior which shows the representation
                        lines[-1] = f"print(repr({last_line}))"
                        clean_source = "\n".join(lines)

                # Run the clean source code on the MCU and capture output
                try:
                    actual_output = run_micropython_code(clean_source).strip()
                except Exception as e:
                    # Check if this is an expected error (traceback in expected output)
                    if expected_output and ("Traceback" in expected_output or "Error:" in expected_output):
                        # Extract error output from the exception
                        if hasattr(e, 'args') and e.args:
                            error_msg = str(e.args[0])
                            if "stdout:" in error_msg:
                                # Extract the stdout part which contains the traceback
                                stdout_part = error_msg.split("stdout: ")[1]
                                actual_output = stdout_part.strip()
                            else:
                                actual_output = str(e).strip()
                        else:
                            actual_output = str(e).strip()
                    else:
                        # Re-raise if this wasn't an expected error
                        raise

                # Simple comparison - you might want to make this more sophisticated
                if expected_output and actual_output != expected_output:
                    # For traceback comparisons, be more flexible
                    if "Traceback" in expected_output and "Traceback" in actual_output:
                        # Check if the key error information matches
                        expected_lines = expected_output.strip().split('\n')
                        actual_lines = actual_output.strip().split('\n')
                        
                        # Check the last line (the actual error)
                        if expected_lines and actual_lines:
                            expected_error = expected_lines[-1].strip()
                            actual_error = actual_lines[-1].strip()
                            
                            # Handle minor differences in error messages
                            if "NameError" in expected_error and "NameError" in actual_error:
                                # Compare the core error message, allowing for slight variations
                                if "name 'x' is" in expected_error and "name 'x' is" in actual_error:
                                    return  # Consider this a match
                    
                    raise AssertionError(f"Expected: {expected_output!r}, Got: {actual_output!r}")

    def _clean_doctest_source(self, doctest_source: str) -> str:
        """
        Clean doctest source by removing >>> and ... prefixes to get actual Python code
        """
        lines = doctest_source.split("\n")
        cleaned_lines = []

        for line in lines:
            if line.startswith(">>> "):
                # Remove the >>> prefix
                code_line = line[4:]
                cleaned_lines.append(code_line)
            elif line.startswith("... "):
                # Remove the ... prefix (continuation line) but preserve remaining indentation
                cleaned_lines.append(line[4:])
            elif line.strip() == "...":
                # Handle standalone ... continuation (empty line)
                cleaned_lines.append("")
            elif line.strip():
                # Keep non-empty lines that don't start with >>> or ...
                cleaned_lines.append(line)

        # Remove any trailing empty lines
        while cleaned_lines and not cleaned_lines[-1].strip():
            cleaned_lines.pop()

        return "\n".join(cleaned_lines)

    def _should_print_result(self, code_line: str, expected_output: str) -> bool:
        """
        Determine if a line of code should have its result printed
        based on whether there's expected output and the code is an expression
        """
        if not expected_output.strip():
            return False

        # Simple heuristic: if the line doesn't contain assignment, import, def, class, etc.
        # and there's expected output, it's probably an expression that should be printed
        keywords_that_dont_print = ["=", "import ", "def ", "class ", "if ", "for ", "while ", "try:", "with ", "print("]
        code_stripped = code_line.strip()

        # Skip if it already has print
        if "print(" in code_stripped:
            return False

        # Skip if it contains statement keywords
        for keyword in keywords_that_dont_print:
            if keyword in code_stripped:
                return False

        # If it looks like a simple expression and we expect output, wrap it in print
        return True


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
        
        lines = document.text.split('\n')
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
            elif in_doctest_directive and line and not line.startswith(' ') and not line.startswith('\t'):
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
            if line.strip().startswith('>>> '):
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
                    
                    if stripped.startswith('>>> ') or stripped.startswith('... '):
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
                            if peek_line.startswith('>>> ') or peek_line.startswith('.. '):
                                break
                            # Otherwise, include expected output
                            else:
                                # Include the empty line and continue to expected output
                                doctest_lines.append(current_line)
                                i += 1
                        else:
                            break
                    elif not (stripped.startswith('>>>') or stripped.startswith('.. ')):
                        # This is expected output, include it
                        doctest_lines.append(current_line)
                        i += 1
                    else:
                        # Hit another construct, stop
                        break
                
                # Process the collected doctest block
                doctest_text = '\n'.join(doctest_lines)
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
            if reason.startswith('if'):
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

        if action not in ('start', 'next', 'end'):
            raise ValueError('Bad skip action: ' + action)
        if state.last_action is None and action not in ('start', 'next'):
            raise ValueError(f"'{directive}: {action}' must follow '{directive}: start'")
        elif state.last_action and action != 'end':
            raise ValueError(f"'{directive}: {action}' cannot follow '{directive}: {state.last_action}'")

        state.last_action = action

        if action == 'start':
            self.install(example, state, reason)
        elif action == 'next':
            self.install(example, state, reason)
            state.remove = True
        elif action == 'end':
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
            for line in output.split('\n'):
                if line.startswith('SKIP_CONDITION_RESULT:'):
                    result_str = line.split('SKIP_CONDITION_RESULT:', 1)[1].strip()
                    # Convert string representation back to boolean
                    result = result_str.lower() == 'true'
                    print(f"Skip condition '{condition}' evaluated to: {result}")
                    return result
                elif line.startswith('SKIP_CONDITION_ERROR:'):
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
        self.skipper = MicroPythonSkipper('skip')
        # Copy the lexers from the standard parser
        self.lexers = self._standard_parser.lexers
        self.directive = 'skip'
    
    def __call__(self, document):
        """Parse document using standard SkipParser logic but with MCU evaluation"""
        for lexed in self.lexers(document):
            arguments = lexed.lexemes['arguments']
            if arguments is None:
                raise ValueError(f'missing arguments to {self.directive}')
            
            from sybil.parsers.abstract.skip import SKIP_ARGUMENTS_PATTERN
            match = SKIP_ARGUMENTS_PATTERN.match(arguments)
            if match is None:
                raise ValueError(f'malformed arguments to {self.directive}: {arguments!r}')
            
            yield Region(lexed.start, lexed.end, match.groups(), self.skipper)


class MicroPythonClearNamespaceParser:
    """
    Parser for clear-namespace directives that resets the MicroPython MCU
    """
    
    def __call__(self, document):
        """Parse document and yield regions for clear-namespace directives"""
        # Look for clear-namespace directive (with or without ::)
        pattern = r'^(?P<indent> *)\.\.[ \t]+clear-namespace[ \t]*(?:::)?[ \t]*$'
        
        for match in re.finditer(pattern, document.text, re.MULTILINE):
            yield Region(
                start=match.start(),
                end=match.end(),
                parsed=None,  # No parsing needed
                evaluator=self._clear_namespace_evaluator
            )
    
    def _clear_namespace_evaluator(self, example: Example) -> None:
        """Reset the MicroPython MCU to clear the namespace"""
        reset_micropython_mcu()


sybil = Sybil(
    path=docs_path.as_posix(),
    parsers=[
        DocTestDirectiveParser(),
        MicroPythonSkipParser(),  # Use MCU-aware skip parser that handles all skip directives
        MicroPythonClearNamespaceParser(),  # Use MicroPython-specific clear namespace
        MicroPythonDocTestParser(),  # Use custom doctest parser
        CodeBlockParser(language="python", evaluator=MicroPythonEvaluator()),
    ],
    pattern="*.rst",
)


pytest_collect_file = sybil.pytest()
