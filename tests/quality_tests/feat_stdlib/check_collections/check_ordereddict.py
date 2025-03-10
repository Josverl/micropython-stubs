from collections import OrderedDict


d1 = OrderedDict()
d1["a"] = 1
d1["b"] = 2

d2 = OrderedDict({"a": 1, "b": 2})
d2["c"] = 3

# To make benefit of ordered keys, OrderedDict should be initialized
# from sequence of (key, value) pairs.
# issue https://github.com/Josverl/micropython-stubs/issues/789
d3 = OrderedDict(
    [("z", 1), ("a", 2)]  # stubs-ignore: version < 1.24.0
)  
d3 = OrderedDict()


d3["w"] = 5
d3["b"] = 3
for k, v in d3.items():
    print(k, v)
