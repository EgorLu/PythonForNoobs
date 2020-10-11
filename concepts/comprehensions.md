# Comprehensions

Comprehensions in Python are syntactic constructs for creating new sets, lists, dictionaries or even generators,
based on existing iterables.

In Python, short and readable, one-line comrehensions can replace multi-line loops.
Thus improving the code's readability.

Comprehensions follow the set-builder notation from the mathematical set-theory:

```
{x | x E N, x > 0}
```

- `x` is the output expression (what we want the element to look like)
- `x E N` is the input set (take x from N)
- `x > 0` is the predicate (the condition, in our example we only pick positive values)

Following this example, our set would be an infinite set of positive integers `{1, 2, 3, 4, 5, 6, 7, ...}`

**Syntax:**

In Python the syntax very much resembles the mathematical syntax but uses words instead of symbols.

```python
{x for x in N if x > 0}
```

**Examples:**

```python
my_list = [1, 2, 3, 4, 5]

[num for num in my_list] # [1, 2, 3, 4, 5] (we coppied the entire list)
[num * 2 for num in my_list] # [2, 4, 6, 8, 10] (the output expression is num*2, thus every item was multiplied)
[num for num in my_list if num > 2] # [3, 4, 5] (only numbers larger than 2 were picked)
```

For instance, we could easily get a list of even numbers by using a list comprehension:
```python
all_numbers = [1, 7, 4, 6, 3, 19, 8]

even_numbers = [n for n in all_numbers if n % 2 == 0] # [4, 6, 8]
```

Or in case we had two lists, of all the tasks that need to be done, and other list of tasks that were completed,
we could make a new list of the remaning tasks:

```python
all_tasks = ['wake up', 'brush teeth', 'walk with the dog', 'drink coffee', 'spread misinformation on the internet']
completed_tasks = ['wake up', 'drink coffee']
remaining_tasks = [task for task in all_tasks if task not in completed_tasks]
# ['brush teeth', 'walk with the dog', 'spread misinformation on the internet']
```

## Advanced features

### Nested loops

Comprehensions support more than one for loop, allowing loop nesting.

**Example:**

Suppose there is a 2D list (a list in which each element is another list a.k.a list of lists a.k.a matrix)
and we want to flatten it, turning it into just one simple list of elements.

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

This could be done using regular `for` loops:
```python
flat_list = []
for sub_list in matrix:
    for item in sub_list:
        flat_list.append(item)
# flat_list == [1, 2, 3, 4, 5, 6]
```

Instead, a list comprehension can do it in a short, one-liner:
```python
flat_list = [item for sub_list in matrix for item in sub_list] # [1, 2, 3, 4, 5, 6]
```

We could also add a condition. For instance assume we only want odd numers:
```python
flat_list = [item for sub_list in matrix for item in sub_list if item % 2 != 0] # [1, 3, 5]
```

Conditions can also be added between the nested loops like so:
```python
matrix = [ 
    [1, 2], 
    [6, 6, 6], 
    [3, 4], 
    [5, 6], 
    [0] 
]

[item for sub_list in matrix if len(sub_list) == 2 for item in sub_list if item % 2 != 0] # [1, 3, 5]
```

This way we only pick sub-lists that have two elements, and then pick only the odd numbers from them.

### Multiple conditions

It's possible to set more than one condition using the `if` statement.

In such case, they will be treated as the logical `and`.

**Example:**

```python
[n for n in range(100) if n % 2 == 0 if n > 20 if n < 40] # [22, 24, 26, 28, 30, 32, 34, 36, 38]
[n for n in range(100) if n % 2 == 0 and n > 20 and n < 40] # [22, 24, 26, 28, 30, 32, 34, 36, 38]
```

## Important notes

- Comprehensions are part of the core language, they are generally faster than similar functions.
- Comprehensions should stay short and elegant. They can become unreadable if made too long or complex.
- Sometimes giving up on a comprehension and writing the logic in loops can be more readable and easier to think of.