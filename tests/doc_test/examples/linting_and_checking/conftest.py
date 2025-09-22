# from typing import Optional

# from sybil import Sybil, Example
# from sybil.parsers.rest import DocTestParser, PythonCodeBlockParser, CodeBlockParser


# def lint_python_source(example: Example) -> Optional[str]:
#     # here you'd feed example.parsed, which contains the python source of the
#     # .. code-block:: python, to your linting tool of choice
#     pass


# linting = Sybil(
#     name='linting',
#     parsers=[
#         CodeBlockParser(language='python', evaluator=lint_python_source),
#     ],
#     patterns=['*.rst'],
# )

# tests = Sybil(
#     name='tests',
#     parsers=[
#         DocTestParser(),
#         PythonCodeBlockParser(),
#     ],
#     patterns=['*.rst'],
# )

# pytest_collect_file = (linting + tests).pytest()
