import ulab
from typing import List, Union

def clip(x1: Union[ulab.array, float], x2: Union[ulab.array, float], x3: Union[ulab.array, float]) -> ulab.array: ...
def equal(x1: Union[ulab.array, float], x2: Union[ulab.array, float]) -> List[bool]: ...
def not_equal(x1: Union[ulab.array, float], x2: Union[ulab.array, float]) -> List[bool]: ...
def maximum(x1: Union[ulab.array, float], x2: Union[ulab.array, float]) -> ulab.array: ...
def minimum(x1: Union[ulab.array, float], x2: Union[ulab.array, float]) -> ulab.array: ...
