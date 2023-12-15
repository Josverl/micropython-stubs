from collections import namedtuple

MyTuple = namedtuple("MyTuple", ("id", "name"))

t1 = MyTuple(1, "foo") 
t2 = MyTuple(2, "bar") 
print(t1.name)
assert t2.name == t2[1]

print(type(MyTuple))
print(type(t1))
print(type(t2))
