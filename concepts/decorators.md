# Decorators

A decorator in Python, is a function that receives an existing function, extends it somehow and returns
the new, extended function.

**Why it works:**

Functions in Python are first-class objects. Which means that they can be stored as variable values,
passed as arguments to other functions and even returned by other functions.

Furthermore, it's possible to define functions inside other functions.
In such a case the inner function will be bound to the parent function's scope and will cease to exist
when the parent function stops execution.
On the other hand, if the parent function returns a reference (pointer) to the inner function, it may
be used outside of the parent function's scope.

## Explanation

Assume that we have a list of names. Those are people that we want to greet with excitement.
```python
cool_people = ['Jackie Chan', 'Ada Lovelace', 'Guido van Rossum', 'King Leonidas']
```

This people can present themselves though, with this function:
```python
def present_person(name):
    print(f'Hello, my name is {name}!')
```

But we would like to add some hype before each person presents itself. So it will look like this:
```
Ladies and gentleman, please welcome Jackie Chan!
- Hello, my name is Jackie Chan!

Ladies and gentleman, please welcome Ada Lovelace!
- Hello, my name is Ada Lovelace!

Ladies and gentleman, please welcome Guido van Rossum!
- Hello, my name is Guido van Rossum!

Ladies and gentleman, please welcome King Leonidas!
- Hello, my name is King Leonidas!
```

Now, we could create a `for` loop and print our single line of hype and then call `present_person()`,
but what if we will want the same presentation in another part of the program? We will have to rewrite it.
Or what if we don't want all people to be presented one after each other?

In order to solve that, we need a function that will print our hype text and then call `present_person()`.
Basically we want to decorate an existing function with some new functionality.

We could do it like that:
```python
def hyped_presentation(func, name):
    print(f'Ladies and gentleman, please welcome {name}!')
    func(name)

hyped_presentation(present_person, cool_people[0])
# Ladies and gentleman, please welcome Jackie Chan!
# Hello, my name is Jackie Chan!
```

It works, but we need to provide `present_person` as an argument each time, and it's ugly.
Instead we could create a decorated version of `present_person` and use it by only providing a name of the person.

```python
def hyped_presentation(func):
    def decorated_function(name):
        print(f'Ladies and gentleman, please welcome {name}!')
        func(name)
    return decorated_function

hype_person = hyped_presentation(present_person)
hype_person(cool_people[0])
# Ladies and gentleman, please welcome Jackie Chan!
# Hello, my name is Jackie Chan!
```

Now instead of providing the basic function each time, we can use the new, upgraded function that we named `hype_person()`
and only provide it with the name of the person.

This is now a decorated function and `hyped_presentation()` is the decorator function.

**Syntax sugar:**

Python provides a nice syntactic improvement in order to make this proccess shorter and easier to read:
```python
@hyped_presentation
def present_person(name):
    print(f'Hello, my name is {name}!')

present_person(cool_people[0])                                                                                          
#Ladies and gentleman, please welcome Jackie Chan!
#Hello, my name is Jackie Chan!
```

This is the short version and is equivalent to the previous example `present_person = hyped_presentation(present_person)`.

It defines `present_person()` normally, then decorates it and assignes the decorated function to the original name.

**Making the decorator work with other functions**

You may havfe noticed that the inner function named `decorated_function` takes exactly the same arguments as the function
that's being decorated.

But what if we had another function, say `greet_based_on_gender(name, gender)`. A function that prepends the name with "Mr." or "Mrs."
based on their gender.

Instead of changing our wrapper function each time, we could make it generally work with all kinds of arguments:

```python
def hyped_presentation(func):
    def decorated_function(*args, **kwargs):
        print(f'Ladies and gentleman, please welcome our next guest!')
        func(*args, **kwargs)
    return decorated_function

@hyped_presentation
def greet_based_on_gender(name, gender):
    title = 'Mrs.'
    if gender == 'male':
        title = 'Mr.'
    print(f'Hello, I am {title} {name}!')

greet_based_on_gender(cool_people[0], 'male')
# Ladies and gentleman, please welcome our next guest!
# Hello, I am Mr. Jackie Chan!

greet_based_on_gender(cool_people[1], 'female')
# Ladies and gentleman, please welcome our next guest!
# Hello, I am Mrs. Ada Lovelace!
```

Additionally, our previous function would still work:
```python
present_person(cool_people[2])
# Ladies and gentleman, please welcome our next guest!
# Hello, my name is King Leonidas!
```

## Chaining decorators

Decorators in Python can be chained.

Assume that we have a function that adds some swag to another function:
```python
def add_swag(func):
    def wrapper(*args, **kwargs):
        print('---===SWAG===---')
        func(*args, **kwargs)
        print('---===SWAG===---')
    return wrapper
```

We could decorate `present_person()` twice like so:
```python
@add_swag
@hyped_presentation
def present_person(name):
    print(f'Hello, my name is {name}!')

present_person(cool_people[3]) 

# ---===SWAG===---
# Ladies and gentleman, please welcome our next guest!
# Hello, my name is King Leonidas!
# ---===SWAG===---
```

Crazy, ain't it? It's equivalent to `present_person = add_swag(hyped_presentation(present_person))`.

## Good to know

When chaining decorators, the order matters:
```python
@hyped_presentation
@add_swag
def present_person(name):
    print(f'Hello, my name is {name}!')

present_person(cool_people[3])
# Ladies and gentleman, please welcome our next guest!
# ---===SWAG===---
# Hello, my name is King Leonidas!
# ---===SWAG===---
```

It's important to understand the principle of decorators and know how simple and flexible they are.

- The inner, wrapper function can be named as we wish. It doesn't have to be called "inner" or "wrapper".
- Decorated functions can return values, change variable values and do much more than just printing.
- Decorators are just functions that do something before or after a function that they receive as an argument (and run the function itself).

**Learn more** about decorator functionality with the `functools` library.