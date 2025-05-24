"""
Python Variables and Basic Concepts
===================================

This file demonstrates the fundamental concepts of variables in Python.
Python is a dynamically typed language, which means variable types are
determined at runtime, unlike statically typed languages like Java where
types must be declared explicitly.
"""

# Basic Variable Types and Assignment
# -----------------------------------
age = 20          # Integer
price = 19.95     # Float (decimal number)
first_name = 'Mosh'  # String
is_online = False    # Boolean

# Variables can be reassigned
age = 30  # age is now 30
print(f"Current age: {age}")

# Dynamic Typing 
# --------------
"""
Python allows variables to change their type during runtime.
"""
n = 0
print(f'n = {n}')  # n is an integer

n = "abc"
print(f'n = {n}')  # n is now a string

# Multiple Assignments
# --------------------
"""
Python allows multiple variables to be assigned in a single line.
"""
n, m = 0, "abc"  # n is integer, m is string
print(f'n = {n}, m = {m}')

# Increment 
# ---------
"""
There are several ways to increment a number in Python:
1. n = n + 1  (explicit)
2. n += 1     (shorthand)
"""
n = n + 1  # explicit increment
print(f'After increment: {n}')

# Alternative increment syntax
n += 1     # shorthand increment
print(f'After shorthand increment: {n}')

# n++ is bad (doesn't work in Python)

# F-strings (Formatted String Literals)
# ------------------------------------
"""
F-strings (introduced in Python 3.6) are a way to embed expressions
inside string literals. They're called 'f-strings' because you need to
prefix the string with 'f' or 'F'.
"""
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")  # Basic usage

# You can put expressions inside the curly braces
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")  # Using expressions

# Formatting numbers
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # Number formatting

# Null
# ---
x = None # you can't have x