import __future__

import re
import subprocess
import tempfile
from doctest import DocTestParser as StdDocTestParser
from pathlib import Path

import pytest
from sybil import Example, Region, Sybil
from sybil.evaluators.python import pad
from sybil.parsers.rest import CodeBlockParser
from sybil.typing import Evaluator

docs_path = (Path(__file__).parent / "micropython/docs")
docs_path = (Path(__file__).parent / "examples")


def run_micropython_code(source: str) -> str:
    """Run source code on MCU and return the output"""
    try:
        with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as tf:
            tf.write(source)
            tf.close()
            cmd = ['mpremote', "resume", "run", tf.name]
            print ("Running:", " ".join(cmd))
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"mpremote exited with code {e.returncode}, stderr: {e.stderr}, stdout: {e.stdout}")
    finally:
        # housekeeping
        Path(tf.name).unlink()



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
                if expected_output and self._should_print_result(clean_source.split('\n')[-1], expected_output):
                    lines = clean_source.split('\n')
                    last_line = lines[-1].strip()
                    if last_line and not any(keyword in last_line for keyword in ['print(', '=']):
                        # Use repr() to match doctest behavior which shows the representation
                        lines[-1] = f'print(repr({last_line}))'
                        clean_source = '\n'.join(lines)
                
                # Run the clean source code on the MCU and capture output
                actual_output = run_micropython_code(clean_source).strip()
                
                # Simple comparison - you might want to make this more sophisticated
                if expected_output and actual_output != expected_output:
                    raise AssertionError(f"Expected: {expected_output!r}, Got: {actual_output!r}")
    
    def _clean_doctest_source(self, doctest_source: str) -> str:
        """
        Clean doctest source by removing >>> and ... prefixes to get actual Python code
        """
        lines = doctest_source.split('\n')
        cleaned_lines = []
        
        for line in lines:
            if line.startswith('>>> '):
                # Remove the >>> prefix
                code_line = line[4:]
                cleaned_lines.append(code_line)
            elif line.startswith('... '):
                # Remove the ... prefix (continuation line) but preserve remaining indentation
                cleaned_lines.append(line[4:])
            elif line.strip() == '...':
                # Handle standalone ... continuation (empty line)
                cleaned_lines.append('')
            elif line.strip():
                # Keep non-empty lines that don't start with >>> or ...
                cleaned_lines.append(line)
        
        # Remove any trailing empty lines
        while cleaned_lines and not cleaned_lines[-1].strip():
            cleaned_lines.pop()
            
        return '\n'.join(cleaned_lines)

    def _should_print_result(self, code_line: str, expected_output: str) -> bool:
        """
        Determine if a line of code should have its result printed
        based on whether there's expected output and the code is an expression
        """
        if not expected_output.strip():
            return False
            
        # Simple heuristic: if the line doesn't contain assignment, import, def, class, etc.
        # and there's expected output, it's probably an expression that should be printed
        keywords_that_dont_print = ['=', 'import ', 'def ', 'class ', 'if ', 'for ', 'while ', 'try:', 'with ', 'print(']
        code_stripped = code_line.strip()
        
        # Skip if it already has print
        if 'print(' in code_stripped:
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
        
        # Find doctest blocks using a more comprehensive regex
        # This pattern matches >>> followed by any content until the next >>> or end of text
        pattern = r'(>>> .+?)(?=\n>>> |\n\n[A-Za-z]|\Z)'
        
        for match in re.finditer(pattern, document.text, re.MULTILINE | re.DOTALL):
            doctest_text = match.group(1)
            examples = parser.get_examples(doctest_text)
            
            if examples:
                yield Region(
                    start=match.start(),
                    end=match.end(),
                    parsed=examples,
                    evaluator=self.evaluator
                )


sybil = Sybil(
    path=docs_path.as_posix(),
    parsers=[
        MicroPythonDocTestParser(),  # Use custom doctest parser
        CodeBlockParser(language='python', evaluator = MicroPythonEvaluator()),
    ],
    pattern='*.rst',
)


pytest_collect_file = sybil.pytest()