from collections import OrderedDict

# To make benefit of ordered keys, OrderedDict should be initialized
# from sequence of (key, value) pairs.
d = OrderedDict([("z", 1), ("a", 2)])  # stubs-ignore: port in ["samd"]
# More items can be added as usual

d["w"] = 5
d["b"] = 3
for k, v in d.items():
    print(k, v)
