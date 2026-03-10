# ------------------
# Basic Iterator Usage
# ------------------

# 1. Given the list below:
numbers = [10, 20, 30]

# Create an iterator using iter()
# Use next() to print each element manually


# 2. Given the string:
text = "PYTHON"

# Create an iterator from the string
# Print the first three characters using next()


# 3. Create a list:
values = [5, 15, 25, 35]

# Create an iterator
# Print two elements using next()
# Then print the remaining elements using a for loop


# ------------------
# Understanding StopIteration
# ------------------

# 4. Create a list with two elements
# Use iter() and next() to retrieve both elements
# Try calling next() again and observe the StopIteration error


# 5. Rewrite the previous exercise using try/except
# Catch the StopIteration exception and print:
# "Iterator finished"


# ------------------
# Manual Iteration Loop
# ------------------

# 6. Given the list:
numbers = [1, 2, 3, 4]

# Create an iterator
# Use a while True loop with try/except
# Manually print all elements using next()


# ------------------
# Iterators With Built-in Functions
# ------------------

# 7. Given:
numbers = [1, 2, 3, 4]

# Use map() to create an iterator that squares the numbers
# Use next() to print the first two results


# 8. Given:
numbers = [10, 15, 20, 25]

# Use filter() to create an iterator that keeps only numbers > 15
# Convert the iterator to a list and print it


# ------------------
# Creating a Custom Iterator
# ------------------

# 9. Create a class CountDown
# The iterator should count down from a starting number to 1
#
# Example:
# CountDown(5)
# Output:
# 5
# 4
# 3
# 2
# 1


# 10. Create a class EvenNumbers
# The iterator should generate even numbers from 0 up to a limit
#
# Example:
# EvenNumbers(10)
# Output:
# 0, 2, 4, 6, 8, 10


# ------------------
# More Control Over Iteration
# ------------------

# 11. Create a class StepCounter
# It should count from a start value to a limit
# increasing by a custom step.
#
# Example:
# StepCounter(start=0, step=3, limit=12)
# Output:
# 0, 3, 6, 9, 12


# ------------------
# Thinking Like Python
# ------------------

# 12. Create an iterator class ReverseList
# It should iterate through a list in reverse order.
#
# Example:
# ReverseList([1, 2, 3])
# Output:
# 3, 2, 1


# ------------------
# Iterator State
# ------------------

# 13. Create a class RepeatValue
# It should repeat a given value a specific number of times.
#
# Example:
# RepeatValue("A", 3)
# Output:
# A, A, A


# ------------------
# Combining Ideas
# ------------------

# 14. Create a class FibonacciIterator
# It should generate the Fibonacci sequence up to n numbers.
#
# Example:
# FibonacciIterator(7)
# Output:
# 0, 1, 1, 2, 3, 5, 8


# ------------------
# Bonus Challenge
# ------------------

# 15. Create a class RangeLike
# Implement your own version of Python's range().
#
# It should support:
# start
# stop
# step
#
# Example:
# RangeLike(2, 10, 2)
# Output:
# 2, 4, 6, 8
#
# Use the iterator protocol (__iter__ and __next__)
