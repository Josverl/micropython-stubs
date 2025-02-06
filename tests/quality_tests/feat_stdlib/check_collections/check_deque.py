from collections import deque

# Creating a deque
queue = deque(["name", "age", "DOB"])
print(queue)  # Output: deque(['name', 'age', 'DOB'])

# Appending items
queue.append("address")
queue.appendleft("ID")
print(queue)  # Output: deque(['ID', 'name', 'age', 'DOB', 'address'])

# Popping items
queue.pop()
queue.popleft()
print(queue)  # Output: deque(['name', 'age', 'DOB'])

# Extending deque
queue.extend(["address", "phone"])
print(queue)  # Output: deque(['name', 'age', 'DOB', 'address', 'phone'])

# Removing items
queue.remove("age")

# Reversing deque
queue.reverse()  # type: ignore
