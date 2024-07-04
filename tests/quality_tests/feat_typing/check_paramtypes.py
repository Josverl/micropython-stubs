from typing import Any, Dict, List

from typing_extensions import TYPE_CHECKING


def add_numbers(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f"Hello, {name}!")

def get_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def process_data(data: Dict[str, Any]) -> None:
    # process the data
    pass
