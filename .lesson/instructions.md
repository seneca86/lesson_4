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

Indentation goes into deeper levels when we write embedded clauses:

```python
clouds = False
cold = False

if clouds:
    if cold:
        print('winter')
    else:
        print('summer')
else:
    if cold:
        print('spring')
    else:
        print('summer')
```

We can think of this chunk of code as a three-step process: assigning a value to two booleans, then performing a conditional comparison, then calling the `print()` statement. The important thing is that indentation determines how the `if` and `else` sections are paired.

When we need to discern among more than two cases, we will use the `elif` clause, which is a shortcut for `else` plus `if`.

```python
day = 'Monday'
if day == 'Monday':
    print('first')
elif day == 'Tuesday':
    print('second')
elif day == 'Wednesday':
    print('third')
elif day == 'Thursday':
    print('fourth')
elif day == 'Friday':
    print('fifth')
elif day == 'Saturday':
    print('sixth')
elif day == 'Sunday':
    print('seventh')
```

Besides `==`, there are other _comparison operators_:

| Operator | Symbol |
|----------|--------|
| equality | `==`|
| inequality | `!=`|
| less than | `<`|
| less than or equal to |`<=`|
| greater than | `>`|
| greater than or equal to |`>=`|

Additionally, the logical operators `or`, `not`, `and` allow us to make multiple comparisons simultaneously.

```python
x = 3
5 > x
x == 4
x < 10
(x < 10) and (x <  20)
(x < 10) and not (x == 4)
(x < 10) or (x > 10)
1 < x < 10
1 < x < 10 < 20
```

In the last two lines, note how Python allows us to compress multiple comparison in a concise way.

## Conventions about `True`

Python can evaluate the "truthiness" of a variable even if it is not a boolean. In general, a variable that exists and is not zero or empty will be `True`. More precisely, everything is `True` except for `False`, `None`, `0`, `0.0`, `''`, `{}`, `[]`, `{}`, and `set()`.

## Multiple comparisons with `in`

When we want to check whether a value belongs to a set of values, `if` clauses can involve a lot or `or`s and get long. The `in` membership operator is useful for these situations.

```python
name = 'Bob'
beatles = 'John', 'Paul', 'George', 'Ringo'
name in beatles 
```

Note how easy it is to check whether the value is one of those listed. But, what type of variable is the one we just used? It is a `tuple` and we will come back to it given its importance. `tuple`'s are typically enclosed by parenthesis, but they can be omitted as in the example.

## Assignment expressions with the walrus operator

The walrus operator is the funny name for `:=`, which looks like a walrus sideways. It was introduced recently in Python, although it existed in other programming languages. It is useful for assignment expressions and we will revisit it later.

A (traditional) **assignment statement** is a statement in which we assign a value to an object, e.g. `a = 1 + 1`. An **expression** is a special statement that can be evaluated to some value, like `1 + 1`.

An **assignment expression** is similar to an **assignment statement** but it also returns the value. This subtle difference enables several simplifications in loops and in conditional statements such as the following:

```python

```