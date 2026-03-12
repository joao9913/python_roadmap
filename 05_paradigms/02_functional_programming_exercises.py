from functools import reduce


# ------------------
# Lambda Functions
# ------------------

# 1. Create a lambda function that takes a number and returns True if it is positive.
# Test it with several values.

print("#1")



print()


# 2. Create a lambda function that returns the length of a string.
# Test it on a list of words using map().

print("#2")

words = ["developer", "python", "code", "functional"]



print()


# ------------------
# map()
# ------------------

# 3. Given a list of prices, use map() to add a 20% tax to each price.
# Return the new list.

print("#3")

prices = [10, 25, 40, 100]



print()


# 4. Given a list of usernames, use map() to convert them into dictionaries
# with the structure:
# {"username": "<name>"}

print("#4")

usernames = ["alice", "bob", "charlie"]



print()


# ------------------
# filter()
# ------------------

# 5. Given a list of file names, use filter() to keep only files that end with ".py".

print("#5")

files = ["app.py", "config.json", "database.py", "notes.txt"]



print()


# 6. Given a list of users represented as dictionaries,
# filter users who are active.

print("#6")

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
]



print()


# ------------------
# reduce()
# ------------------

# 7. Given a list of numbers, use reduce() to calculate the total sum.

print("#7")

numbers = [5, 10, 15, 20]



print()


# 8. Given a list of strings, use reduce() to join them into one sentence
# separated by spaces.

print("#8")

words = ["Functional", "programming", "is", "powerful"]



print()


# ------------------
# Higher-Order Functions
# ------------------

# 9. Write a function apply_operation(func, value)
# that applies the given function to the value and returns the result.
# Test it with at least two different functions.

print("#9")



print()


# 10. Write a function transform_list(data, func)
# that applies a function to every element of the list using map()
# and returns the result.

print("#10")

data = [1, 2, 3, 4]



print()


# ------------------
# Function Composition
# ------------------

# 11. Write a function compose(f, g)
# that returns a new function equivalent to f(g(x)).

print("#11")



print()


# 12. Create two functions:
# - strip_spaces(text)
# - make_lower(text)
#
# Use your compose() function to combine them so that the final function
# cleans a string by stripping spaces and converting it to lowercase.

print("#12")



print()


# ------------------
# Data Transformation (Realistic Tasks)
# ------------------

# 13. Given a list of product dictionaries, use functional tools
# to create a list of only the product names.

print("#13")

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
]



print()


# 14. Using filter(), create a list of products that cost more than 100.

print("#14")



print()


# 15. Using map(), create a list with the prices of all products
# after applying a 10% discount.

print("#15")



print()


# ------------------
# Functional Pipelines
# ------------------

# 16. Starting from the list below:
# - Convert all numbers to their absolute value
# - Keep only numbers greater than 10
# - Square the remaining numbers
#
# Use a pipeline with map() and filter().

print("#16")

numbers = [-20, -5, 3, 12, 15, -30]



print()


# 17. From a list of sentences, produce a list containing
# the length of each sentence.

print("#17")

sentences = [
    "Functional programming is powerful",
    "Python supports multiple paradigms",
    "Write clean code",
]



print()


# ------------------
# Immutability Practice
# ------------------

# 18. Given a list of dictionaries representing users:
# Create a NEW list where each user has a new field:
# "role": "user"
#
# Do not modify the original list.

print("#18")

users = [
    {"name": "Alice"},
    {"name": "Bob"},
]



print()


# ------------------
# Harder Challenges (Interview Style)
# ------------------

# 19. Given a list of log entries:
# Count how many times each log level appears.
#
# Example output:
# {"INFO": 2, "ERROR": 1, "WARNING": 1}
#
# Use reduce().

print("#19")

logs = ["INFO", "ERROR", "INFO", "WARNING"]



print()


# 20. Build a functional pipeline that:
# - Takes a list of numbers
# - Removes duplicates
# - Keeps only numbers divisible by 5
# - Multiplies each by 10
# - Returns the final list

print("#20")

numbers = [5, 10, 15, 10, 20, 25, 30, 30]



print()
