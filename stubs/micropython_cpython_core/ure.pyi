
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def compile(pattern: Any, flags: Any=0) -> Any: ...
    #   0: return re.compile(pattern,flags|re.DOTALL)
    # ? 0: return re.compile(pattern, flags|re.DOTALL)
def match(pattern: Any, string: Any) -> Any: ...
    #   0: return re.match(pattern,string,re.DOTALL)
    # ? 0: return re.match(pattern, string, re.DOTALL)
def search(pattern: Any, string: Any) -> Any: ...
    #   0: return re.search(pattern,string,re.DOTALL)
    # ? 0: return re.search(pattern, string, re.DOTALL)
def sub(pattern: Any, repl: Any, string: Any, count: Any=0, flags: Any=0) -> Any: ...
    #   0: return re.sub(pattern,repl,string,count,flags|re.DOTALL)
    # ? 0: return re.sub(pattern, repl, string, count, flags|re.DOTALL)
