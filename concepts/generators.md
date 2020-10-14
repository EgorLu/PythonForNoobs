# Generators

Generators are functions that behave like "lazy iterables".

Practically a generator is a function, that has a `yield` keyword instead of the normal `return` statement.

This causes the function to pause execution at the `yield` command, and resume to it once it's called again.

The generator returns an iterable, which interacts with the built-in `next()` function.

**Example:**

```python
def my_gen():
    counter = 0
    while True:
        yield counter
        counter += 1

g = my_gen()

next(g) # 0
next(g) # 1
next(g) # 2
next(g) # 3
```

This way generators are able to produce infinite sequences of items without hurting the performance.

Unlike data structures akin lists, generators do not store their values in memory and the value is
being computed only on demand (a.k.a "lazy") and never beforehand.

# Looping over iterators

Since the value returned by the generator function follows the iterator protocol, it's possible to use
the regular looping tools with the iterator instead of repeatedly calling the `next()` function.

**Example:**

```python
def my_gen():
    word = 'banana'
    for c in word:
        yield c

letters = my_gen()

for l in letters:
    print(l)
# b
# a
# n
# a
# n
# a
```

# Generator comprehension

Also called "generator expressions", allow creating generators in as short as one line of code.

**Example:**

```python
letters = (c for c in 'banana')
```

# More about `yield`

First of all, `yield` is an expression a not a statement. It's frequently used as a statement (just like `return`),
but it also produces a value just like an expression. This value can be used in the generator function itself.

Practically the `yield` expression acts like a pipe between the generator function and the outer scope in which the
returned iterator resides.

At first, `yield` returns the iterator with the data. Then the iterator can send data back via the `.send()` method.

**Example:**

```python
def my_gen():
    counter = 0
    while True:
        yield_value = yield counter
        counter += yield_value
```

Side note - in this example it would be better to check that `yield_value is not None`.
For example `counter += yield_value if yield_value else 0`.

A `None` value will be automatically sent back to the generator function if the `.send()` method wasn't invoked.

```python
g = my_gen()

next(g) # 0
g.send(5) # 5
g.send(3) # 8
next(g) # 8
```

This is the way we can create coroutines in Python, but this is another topic.

# Todo:
Explain about `.throw()` and `.close()`.