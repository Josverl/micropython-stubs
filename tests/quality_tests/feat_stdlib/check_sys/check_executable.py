import sys

from typing_extensions import assert_type, get_type_hints

# these should be invalid
x = sys.executable # pyright: ignore [reportGeneralTypeIssues]

