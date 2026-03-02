"""
01_if_statements.py
Topic: If Statements (Conditional Logic)
Goal: Understand conditional execution, comparison operators, logical operators, nesting and truthiness
"""

# ------------------
# Basic If Statement
# ------------------

age = 18

if age >= 18:
    print("You are an adult")

# Code inside the block executes only if the condition is True
# Identation defines the block


# ------------------
# If / Else
# ------------------

temperature = 15

if temperature > 20:
    print("Warm weather")
else:
    print("Cold weather")

# Else runs if the condition is false


# ------------------
# If / Elif / Else
# ------------------

score = 85

if score >= 90:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print ("Grade C")

# Conditions are evaluated top to bottom
# First True condition executes, the rest are skipped


# ------------------
# Comparison Operators
# ------------------

a = 10
b = 20

print(a == b)   # Equal
print(a != b)   # Not Equal
print(a > b)    # Greater Than
print(a < b)    # Less than
print(a >= b)   # Greater or equal
print(a <= b)   # Less or equal


# ------------------
# Logical Operators
# ------------------

x = 10

if x > 5 and x < 15:
    print("x is between 5 and 15")

if x < 5 or x > 8:
    print("x satisfies OR condition")

if not x == 10:
    print("x is not 10")

# and - both conditions must be True
# or - at least on condition must be True
# not - negates the condition


# ------------------
# Truthiness
# ------------------

value = ""

if value:
    print("This will not print")
else:
    print("Empty values are False")


# ------------------
# Nested If Statements
# ------------------

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young")

# Nested conditionals allow multi-level decision


# ------------------
# One Line Conditional (Ternary Operador)
# ------------------

age = 16

status = "Adult" if age >= 18 else "Minor"
print(status)

# Syntax: value_if_true if condition else value_if_else


# ------------------
# Membership Testing
# ------------------

name = "Joao"

if "J" in name:
    print("Name contains J")

numbers = [1, 2, 3]

if 2 in numbers:
    print("2 exists in list")

# in checks membership in sequences and collections


# ------------------
# Identity Comparison
# ------------------

value = None

if value is None:
    print("Value is None")

# Use is when checking against None
# Do not use "==" for identity checks


# ------------------
# Chained Comparisons
# ------------------

num = 10

if 5 < num < 20:
    print("Number is within range")

# Equivalente to: num > 5 and num < 20


# ------------------
# Common Mistakes
# ------------------

# 1. Using = instead of ==
# if age = 18:

# 2. Incorrect indendation
# Python uses indentation to define blocks

# 3. Overlapping conditions in wrong order

score = 95

if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")

# This will never print "Excellent"
# Order matters. Most specific conditions should come first