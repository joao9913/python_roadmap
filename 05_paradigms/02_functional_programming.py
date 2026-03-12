"""
02_functional_programming.py
Topic: Functional Programming
Goal: Understand the basics of functional programming in Python and how to use functions as first-class objects, immutability and higher-order functions
"""

# ------------------
# What Is Functional Programming
# ------------------

# Functional programming is a paradigm where programs are constructed
# by applying and composing functions
# Key characteristics:
# - Functions are first-class citizens (can be passed as arguments, returned from other functions)
# - Immutability: Avoid changing state or variables
# - Pure functions: Output depends only on input, with no side-effects
# - Higher-order functions: Functions that take other functions as input or return functions
# - Function composition: Combining simple functions to build more complex ones

# Functional programming emphasizes **declarative programming**: what to do, not how to do it


# ------------------
# Functions Are First-Class Citizens
# ------------------

def greet(name):
    return f"Hello {name}!"

say_hello = greet   # Assigning function to a variable
print(say_hello("Joao"))

def run_function(func, value):
    print(func(value))

run_function(greet, "Alice")    # Passing function as argument

print("\n-------------------------------------------------------------\n")


# ------------------
# Lambda (Anonymous) Functions
# ------------------

# A lambda functions is a small anonymous function defined in a single line

square = lambda x: x ** 2
print(square(5))

add = lambda x, y: x + y
print(add(3, 4))

print("\n-------------------------------------------------------------\n")


# ------------------
# Higher-Order Functions
# ------------------

# A higher-order function takes functions as arguments or returns a function

def apply_twice(func, value):
    return func(func(value))

double = lambda x: x * 2
print(apply_twice(double, 5))   # double(double(5)) -> 20


def compose(f, g):
    return lambda x: f(g(x))

f = lambda x: x + 3
g = lambda x: x * 2
h = compose(f, g)   # h(x) = f(g(x))

print(h(4)) # (4*2) + 3 = 11

print("\n-------------------------------------------------------------\n")


# ------------------
# Map, Filter, Reduce
# ------------------

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map() applies a function to all elements
squared = list(map(lambda x: x ** 2, numbers))
print("Squared: ", squared)

# filter() selects elements based on a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers: ", evens)

# reduce() accumulates a result by applying a function cumulatively
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers: ", product)

# Combining map, filter, reduce
sum_even_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print("Sum of squares of even numbers: ", sum_even_squares)

print("\n-------------------------------------------------------------\n")


# ------------------
# Immutability
# ------------------

# In FP, variables are not usually modified, use new variables for results

original_list = [1, 2, 3]
new_list = list(map(lambda x: x * 2, original_list))    # original_list remains unchaged
print("Original: ", original_list)
print("New: ", new_list)

print("\n-------------------------------------------------------------\n")


# ------------------
# Functional Pipelines
# ------------------

# You can chain map, filter, reduce to process data in a declarative way

pipeline_result = reduce(
    lambda x, y: x * y,
    filter(lambda x: x % 3 == 0,
           map(lambda x: x * 2, range(1, 11)))
)

print("Pipeline result: ", pipeline_result)

print("\n-------------------------------------------------------------\n")


# ------------------
# When To Use Functional Programming
# ------------------

# - Data transformation (lists, dicts)
# - Stateless operations
# - Situations requiring concise and declarative code
# - Scenarios where functions are naturally composable

# Advantages:
# - Easier to reason about due to pure functions
# - Less side-effects
# - Can lead to shorts and cleaner code


# ------------------
# Summary
# ------------------

# Functional programming:
# - Treats functions as first-class citizens
# - Encourages immutability and pure functions
# - Uses higher-order functions, lambdas and function composition
# - Works well for data processing and declarative code
