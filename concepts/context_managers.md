# Context Managers

Context managers in Python are very comfortable and syntactically pleasing tools of managing such resources as opened files,
database connections, sockets and many more.

An operating system can only have a limited amount of opened files at any given time, this is also true about many other resources.
Therefore it's important to manage these resources carefully and release them (close the connection) when they are not needed.
Otherwise the system will slow down and eventually crash.

**Syntax:**

```python
with context_manager as variable:
    # Main logic goes into the block's body
```

**Example without a context manager:**

We open a file, read it's contents and close it.

```python 
file = open('README.md')
file.read()
file.close()
```

Very simple, yet prone to human errors by forgetting to close the file descriptor.

Python provides us with the `with` statement, which is designed for these kind of tasks exactly.
Open a resource, do something, close it automatically after that something is done.

**Example with a context manager:**

```python
with open('README.md') as file:
    file.read()
```

Voila! We opened a file and assigned it to the `file` variable. Then we do our logic in the indented body of the with block
and as soon as that logic ends the context manager will automatically close the file descriptor for us.

In other programming languages this is usually achieved by using exception handling.

## How it works

`with` is an operator that works with context managers - special objects that are aware of their managed resource and do know
how to start and terminate it.

Custom context managers can be created as classes or by using decorated functions.

**Example of a custom context manager using classes:**

```python
class MyContextManager(): 
    def __enter__(self): 
        print('Resource started') 
        return self
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        print('Resource terminated') 
  
  
with MyContextManager() as my_manager: 
    print('Our lovely logic') 

# Resource started
# Our lovely logic
# Resource terminated
```

File handling, like in the previous example, can be easily implemented with the same logic:
`__enter__` opens the file, the body of the `with` block handles the logic and then `__exit_` closes the file.

# Practical demonstration

In the previous examples we ommited the `__init__` method and didn't really manage any resource for the sake of simplicity.

This time let's write a file manager and explain each step:

```python
class MyFileManager(): 
    def __init__(self, file_path, mode): 
        self.file_path = file_path  # Path to the file
        self.mode = mode            # Mode (r/w/a/r+)
        self.file = None            # Actual file descriptor
          
    def __enter__(self): 
        # If there are errors in the `_init_` method, `__enter__` will not be called.
        # Open the file with the desired file mode and assign it to the object's file attribute.
        self.file = open(self.file_path, self.mode)
        # __enter__ returns a value that is then assigned to the variable following the `as` statement.
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        # Exit will always be called as long as the body of the `with` block is reached.
        # This ensures that the resource will be correctly terminated even if the logic encounters errors.
        self.file.close() 
  
# loading a file  
with MyFileManager('README.md', 'r') as file: 
    file.read()
```

## Custom context managers as decorators

Previously we created a customer context manager using a class, this time let's demonstrate an alternative way by using a decorator.

Firstly, `from contextlib import contextmanager`. Then use this decorator with our custom function:

```python
@contextmanager
def MyContextManager():
    print('__enter__')
    yield
    print('__exit__')
```

Everything above `yield` will turn into the `__enter__` and verything below it will transform into `__exit__`.

This is Python's meta-programming - code that changes the code during run time.

The usage remains the same:

```python
with MyContextManager() as my_manager: 
    print('Our lovely logic') 

# __enter__
# Our lovely logic
# __exit__ 
```

This is just a quick way for creating context managers that spares time and lines of code.

## When to use a context manager

Context managers should be used in any case where a repetetive pattern alike "Open then Close" emerges.

Patters like "Connect -> Disconnect", "Start -> Stop", "Setup variables -> Teardown variables" and so on.

Context managers may remind of a [function decorator](https://github.com/EgorLu/PythonForNoobs/blob/main/concepts/decorators.md)
where there's something happening before the main logic and something happens after it.
