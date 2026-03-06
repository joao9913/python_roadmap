"""
05_recursion.py
Topic: Recursion
Goal: Understand how functions can call themselves to solve problems
"""

# ------------------
# What Is Recursion?
# ------------------

# Recursion is when a function calls itself.
# It is useful for solving problems that can be broken into smaller versions of the same problem.

# Every recursive function must have:
# 1. A BASE CASE -> stops the recursion
# 2. A RECURSIVE CASE -> the function calls itself


# ------------------
# Simple Recursion Example
# ------------------

def countdown(n):
    if n == 0:   # Base case
        print("Done")
    else:
        print(n)
        countdown(n - 1)    # Recursive call

countdown(5)


# ------------------
# Factorial Example
# ------------------

# Factorial of n:
# n! = n * (n-1) * (n-2) * ... * 1

# Example
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:  # Base case
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# ------------------
# Recursive Sum
# ------------------

# Calculate the sum of numbers from 1 to n

def recursive_sum(n):

    if n == 1:  # Base case
        return 1

    return n + recursive_sum(n - 1)

print(recursive_sum(5))


# ------------------
# Recursion With Lists
# ------------------

# Recursively sum elements of a list

def sum_list(numbers):
    if len(numbers) == 0:   # Base case
        return 0

    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4]))


# ------------------
# Infinite Recursion (Danger)
# ------------------

# If there is no base case, recursion never stops
# This causes a RecursionError

# Example (DO NOT RUN)

def bad_recursion():
    return bad_recursion()


# ------------------
# When Recursion Is Used
# ------------------

# Recursion is commonly used for:

# - Tree structures
# - File system traversal
# - Divide and conquer algorithms
# - Backtracking algorithms
# - Mathematical problems (factorial, fibonacci)


# ------------------
# Recursive Fibonacci Example
# ------------------
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(n):
    if n <= 1:   # Base case
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


# ------------------
# Recursion vs Loops
# ------------------

# Many recursive problems can also be solved with loops
# Example: factorial using loop

def factorial_loop(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial_loop(5))


# ------------------
# Key Recursion Rules
# ------------------

# 1. Always define a BASE CASE
# 2. Each recursive call must move toward the base case
# 3. Avoid infinite recursion
# 4. Recursion uses the call stack (memory)
