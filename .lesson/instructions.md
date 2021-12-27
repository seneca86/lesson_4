# Conditional statements

## Introduction

Conditional statements may sound familiar from R or other programming languages. They allow us to bifurcate the code depending on whether certain contidion is met. Before jumping to our first conditional statement we need to review a few syntax conventions.

## Indentation

Most programming languages use curly brackets or keywords such as `begin` and `end` to mark off these sections of code (and others such as loops); indentation is recommended for readibility but not mandatory. One of the trademarks of Python is that indentation is mandatory and enough to delimit a program's structure.

## Comments

A comment is a piece of text ignored by the interpreter; it is marked by the `#` (_pound_ or _sharp_ or _hash_) sign at the beginning of a line or after the code and before the comment itself.

Although Python does not support multiline comments, a trick is to use multi-line strings as such: this is achieved with either `'''` or `"""`.

```Python
feet = 6
inches = 2.8 
meters = 0.3048 * feet
meters += 0.0254 * inches # convert from inches to meters
'''
This is a multi-line comment
surrounded by single or
double quotes 
'''
```

## Line continuations

The recommended maximum length of a line in 80 characters. When we need to write lines longer than that we can use the `\` continuation character. For instance:

```python
sum = 1 + \
      2 + \
      3 + \
      4 + \
      5
long_poem = 'Animula, vagula, blandula \
    Hospes comesque corporis \
    Quae nunc abibis in loca \
    Pallidula, rigida, nudula, \
    Nec, ut soles, dabis iocos'
```

A trick that we will use is to use parenthesis smartly to avoid the need for explicitly invoking the `\`:

```python
sum = (1 +
       2 +
       3 +
       4 +
       5)
```

## `if`, `elif`, `else`

We can write our first conditional statement in Python to check the value of a boolean:

```python
bull_market = True
if bull_market:
    print('hold')
else:
    print('sell')
```

Note the absence of curly brackets and parenthesis, and the importance of the indentation, which is recommended to consist of four spaces.

