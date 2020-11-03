# Slicing

Slicing is a powerful feature in Python for extracting sub-sets out of lists, tuples and arrays.
It allows to accomplish what would otherwise take numerous lines of code in just a couple of characters
and looks good doing it.

**Syntax:**

```python
my_list[start:end:step]
```
- *start* - The index from which the sub-list starts (inclusive).
- *end* - The index at which the sub-list ends (exclusive).
- *step* - How many elements to skip.

**Examples:**

```python
my_list = ['a', 'b', 'c', 'd', 'e']
my_list[1:3] # ['b', 'c']
my_list[1:] # ['b', 'c', 'd', 'e']
my_list[:3] # ['a', 'b', 'c']
my_list[:] # ['a', 'b', 'c', 'd', 'e']
my_list[::2] # ['a', 'c', 'e']
```

**Important:**

- The *start* element is inclusive, which means that it will be included in the sub-list.
- The *end* element is exclusive, which menas that it won't be included in the sub-list.
- The *step* element equals to 1 by default and doesn't need to be written always.

## Additional features

All three values in the slicing syntax may be negative, which grand extra abilities:

- *start* - A negative start index starts listing elements from the end of the list.
- *end*  - A negative end index counts elements up until the last number of elements.
- *step* - A negative step reverses the order of the elements in the list.

**Examples:**

```python
my_list = ['a', 'b', 'c', 'd', 'e']
my_list[-1] # ['e'] (the last element)
my_list[-2:] # ['d', 'e'] (the last two elements)
my_list[:-2] # ['a', 'b', 'c'] (everything except the last two elements)

# Negative step:
my_list[::-1] # ['e', 'd', 'c', 'b', 'a'] (the entire list reversed)
my_list[2::-1] # ['c', 'b', 'a'] (the first three elements but reversed)
my_list[:-3:-1] # ['e', 'd'] (the last two elements but reversed)
my_list[-3::-1] # ['c', 'b', 'a'] (everything except the last two elements but reversed)
```
