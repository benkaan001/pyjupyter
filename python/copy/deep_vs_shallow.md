In Python, a shallow copy and a deep copy are two different ways of creating a new copy of an object, especially when the object is a complex data structure like a list or a dictionary that contains nested objects. The main difference between them lies in how they handle the nested objects during the copy process.

1. Shallow Copy:
A shallow copy creates a new object, but it does not create new copies of the nested objects inside the original object. Instead, it copies references to the nested objects. In other words, the shallow copy creates a new top-level object, but the elements inside it still refer to the same objects in memory as the original object.

Example of shallow copy using `copy()` method from the `copy` module:

```python
import copy

original_list = [1, [2, 3], 4]

# Creating a shallow copy of the original_list
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[1][0] = 999

print(original_list)         # Output: [1, [999, 3], 4]
print(shallow_copied_list)   # Output: [1, [999, 3], 4]
```

As you can see, changing the nested list inside the shallow copy also affects the nested list inside the original list because both the original and shallow copied lists share the same reference to the nested list.

2. Deep Copy:
A deep copy, on the other hand, creates a completely independent new object with its own copies of all the nested objects inside the original object. It recursively copies all nested objects, ensuring that any changes made to the deep copy do not affect the original object.

Example of deep copy using `deepcopy()` method from the `copy` module:

```python
import copy

original_list = [1, [2, 3], 4]

# Creating a deep copy of the original_list
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[1][0] = 999

print(original_list)       # Output: [1, [2, 3], 4]
print(deep_copied_list)    # Output: [1, [999, 3], 4]
```

In this case, changing the nested list inside the deep copy does not affect the nested list inside the original list because they are completely independent copies.

In summary, a shallow copy creates a new object but shares references to nested objects with the original, while a deep copy creates a new object and recursively creates independent copies of all nested objects, ensuring complete independence from the original object.