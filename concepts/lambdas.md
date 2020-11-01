# Lambda Functions

In Python a lambda function is a short, anonymous function.

**Syntax:**

```python
lambda args: expression
```

## Anonymous functions

Anonymous functions differ from the regular ones by the sheer fact that they have no name.

Such functions can be assigned to a pointer (variable), but it isn't mandatory, unlike the `def` syntax.

## How short are lambdas?

In Python lambda functions are one expression long.

Thus they are often called lambda expressions.

Since it's an expression, the lambda function always evaluates to (returns) a value.

## Why are they useful?

Some functions, like `map`, take another function as an argument.
Instead of defining this argument funtion separately, it may be convenient to declare it directly in the `map`'s call.

**Example:**

```python
nums = [1, 2, 3]
double_nums = list(map(lambda x: x * 2, nums)) # 2, 4, 6
```

The built-in `map` function applies a function to every element of the provided list. Our lambda function simply receives
a number and returns it multiplied by 2.

PS. This can be easily achieved by [slicing](https://github.com/EgorLu/PythonForNoobs/blob/main/concepts/slicing.md).

## Advanced

**IIFE:**
Immediately invoked function expression (more popular in the JavaScript world) is a function that is being called as soon
as it is being defined.

In Python in can be achived by using the lambda function inside parentheses, thus producing a callable function, and then
immediately invoking it by using another set of parentheses. Like so:

```python
new_num = (lambda a, b: a + b)(10,5) # 15
```
