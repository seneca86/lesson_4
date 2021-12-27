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

