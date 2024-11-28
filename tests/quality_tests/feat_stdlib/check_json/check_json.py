import json
from io import IOBase
from typing import cast

JSON_DATA = """
[
{
    "name": "Fluffy",
    "species": "Dog",
    "age": 3,
    "breed": "Labrador Retriever"
},
{
    "name": "Whiskers",
    "species": "Cat",
    "age": 5,
    "breed": "Siamese"
},
{
    "name": "Staples",
    "species": "Parrot",
    "age": 14,
    "breed": "Blue Norwegian Parrot"
}
]
"""

data = json.loads(JSON_DATA)


json_string = json.dumps(data)  # Convert the data to a JSON string

# Check MicroPython Interface
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "w") as file:
    seps_1 = (",", ":")  # Change the default separators
    reveal_type(seps_1)  # separators: Tuple[str, str]
    s1 = s2 = "?"
    seps_2 = (s1, s2)  # Change the default separators

    json.dump(data, file)
    json.dump(data, file, (",", ":"))
    json.dump(data, file, seps_1)
    json.dump(data, file, seps_2)

with open("data.json") as file:
    data = json.load(file)


# Verify that CPython options are not supported in the stubs
# if type-ignore is not needed this will raise an error in testing

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # type: ignore

with open("data.json") as file:
    data = json.load(file, cls=None)  # type: ignore
    data = json.load(file, object_hook=None)  # type: ignore
    data = json.load(file, object_pairs_hook=None)  # type: ignore
    data = json.load(file, parse_float=None)  # type: ignore
    data = json.load(file, parse_int=None)  # type: ignore
    data = json.load(file, parse_constant=None)  # type: ignore


data = json.loads(JSON_DATA, cls=None)  # type: ignore
data = json.loads(JSON_DATA, object_hook=None)  # type: ignore
data = json.loads(JSON_DATA, object_pairs_hook=None)  # type: ignore
data = json.loads(JSON_DATA, parse_float=None)  # type: ignore
data = json.loads(JSON_DATA, parse_int=None)  # type: ignore
data = json.loads(JSON_DATA, parse_constant=None)  # type: ignore
