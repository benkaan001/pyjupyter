## Common Data Types

| Data Type        | Sequence | Iterator | Convertible to Generator |
|------------------|----------|----------|-------------------------|
| Lists            | Yes      | No       | No                      |
| Tuples           | Yes      | No       | No                      |
| Strings          | Yes      | Yes      | No                      |
| Sets             | No       | Yes      | No                      |
| Dictionaries     | No       | Yes      | No                      |
| Range objects    | Yes      | Yes      | No                      |
| Files (e.g., `open()`)| No   | Yes      | No                      |
| Generator functions (with `yield`) | No | Yes | Yes                     |
| Enumerate objects (from `enumerate()`) | No | Yes | No                      |
| Zip objects (from `zip()`) | No       | Yes      | No                      |

Note:
- A "Sequence" data type represents an ordered collection of items.
- An "Iterator" data type is an object that allows sequential access to elements in a collection.
- "Convertible to Generator" indicates whether the data type can be converted into a generator using generator functions (`yield`).