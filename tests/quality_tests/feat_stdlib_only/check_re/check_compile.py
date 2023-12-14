import re
from typing import Any, List, Union

from typing_extensions import assert_type

# As re doesn't support escapes itself, use of r"" strings is not
# recommended.
regex = re.compile("[\r\n]")

result = regex.split("line1\rline2\nline3\r\n")

assert_type(result, List[Union[str, Any]])

# Result:
# ['line1', 'line2', 'line3', '', '']
