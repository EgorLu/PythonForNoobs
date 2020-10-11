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

TODO

### Multiple conditions

TODO

## Important notes

- Comprehensions are part of the core language, they are generally faster than similar functions.
- Comprehensions should stay short and elegant. They can become unreadable if made too long or complex.
- Sometimes giving up on a comprehension and writing the logic in loops can be more readable and easier to think of.