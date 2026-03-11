"""
03_generator_expressions.py
Topic: Generator Expressions
Goal: Understand what generator expressions are, how to use them, and why they are memory-efficient
"""

# ------------------
# What Is A Generator Expression
# ------------------

# A generator expression is a compact way to create a generator.
# Similar to list comprehensions, but uses parentheses instead of brackets
# They are lazy, meaning they generate values one at a time and do not store all elements in memory

# Example:

gen_exp = (x ** 2 for x in range(5))

print(type(gen_exp))    # <class 'generator'>

for value in gen_exp:
    print(value)


# ------------------
# Syntax Comparison
# ------------------

# List comprehension
squares_list = [x ** 2 for x in range(5)]
print(squares_list) # [0, 1, 4, 9, 16]

# Generator expression
squares_gen = (x ** 2 for x in range(5))
print(squares_gen)  # <generator object>

for val in squares_gen:
    print(val)


# ------------------
# Lazy Evaluation
# ------------------

# Generator expressions only compute values when iterated over

gen = (x ** 2 for x in range(1000)) # No memory used for 1000 elements
print(next(gen))
print(next(gen))
print(next(gen))

# ------------------
# Generator Expressions With Conditions
# ------------------

# You can include an if condition

gen_even_squares = (x ** 2 for x in range(10) if x % 2 == 0)

for val in gen_even_squares:
    print(val)


# ------------------
# Nested Generator Expressions
# ------------------

# Generator expressions can be nested for complex operations

gen_nested = ((i, j) for i in range(3) for j in range(2))

for pair in gen_nested:
    print(pair)


# ------------------
# Using Generator Expressions With Functions
# ------------------

# Functions like sum(), max(), min() work directly with generator expressions

total = sum(x ** 2 for x in range(5))
print(total)

# No need to create a temporary list


# ------------------
# Memory Efficient Example
# ------------------

# Compare list comprehension vs generator expression

list_comp = [x ** 2 for x in range(1_000_000)]   # large memory
gen_expr = (x ** 2 for x in range(1_000_000))   # memory-efficient

print(type(list_comp))
print(type(gen_exp))


# ------------------
# Summary
# ------------------

# Generator expressions are like list comprehensions but lazy
# Use parentheses instead of brackets
# They save memory by generating values one at a time
# Can include conditions and nested loops
# Can be passed directly to functions like sum(), max(), etc
