"""
04_lambda_functions.py
Topic: Lambda Functions
Goal: Understand how to create and use small anonymous functions
"""

# ------------------
# What Is A Lambda Function
# ------------------

# A lambda function is a small anonymous function
# It can have any number of arguments but only one expression
# Lambda functions are typically used for short, simple operations

# Syntax:
# lambda parameters : expression

# Example:

add = lambda a, b: a + b
print(add(2, 3))


# ------------------
# Basic Lambda Example
# ------------------

# Normal function

def square(x):
    return x * x

print(square(4))

# Lambda version

square_lambda = lambda x : x * x
print(square_lambda(4))


# ------------------
# Lambda With Multiple Arguments
# ------------------

multiply = lambda a, b : a * b
print(multiply(3, 5))


# ------------------
# Lambda Inside Another Function
# ------------------

def apply_operation(a, b, operation):
    return operation(a, b)

result = apply_operation(5, 3, lambda x, y: x + y)
print(result)


# ------------------
# Lambda With map()
# ------------------

# map() applies a function to every element in an iterable

numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))

print(squared)


# ------------------
# Lambda with filter()
# ------------------

# filter() keeps elements that satisfy a condition

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)


# ------------------
# Lambda With sorted()
# ------------------

# Lambda is commonly used as a sorting key

people = [
    {"name": "Ana", "age": 25},
    {"name": "Carlos", "age": 30},
    {"name": "Bruno", "age": 25},
]

sorted_people = sorted(people, key=lambda person: person["age"])

print(sorted_people)


# ------------------
# Lambda Returning Boolean
# ------------------

is_even = lambda x: x % 2 == 0

print(is_even(4))
print(is_even(7))


# ------------------
# Lambda In List Comprehension
# ------------------

numbers = [1, 2, 3, 4]

operations = [lambda x: x * 2, lambda x: x * 3]

for operation in operations:
    print(operation(5))


# ------------------
# Lambda Limitations
# ------------------

# Lambda functions:
# - Can only contain ONE expression
# - Cannot contain statements like:
#   - assignment
#   - loops
#   - multiple lines

# This is NOT allowed:

# lambda x:
#   y = x + 1
#   return y

# For complex logic, use a normal function


# ------------------
# When To Use Lambda
# ------------------

# Good uses:
# - Short simple functions
# - One-time functions
# - Sorting keys
# - map/filter

# Avoid when:
# - The logic becomes complex
# - The function needs multiple steps
# - Readibility suffers


# ------------------
# Example Comparison
# ------------------

# Using normal function

numbers = [1, 2, 3]

def double(x):
    return x * 2

result = list(map(double, numbers))
print(result)

# Using lambda

result = list(map(lambda x: x * 2, numbers))
print(result)
