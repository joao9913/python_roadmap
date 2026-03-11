# ------------------
# Basic Generator Usage
# ------------------

# 1. Create a simple generator function that yields numbers 1, 2, 3
# Use next() to print each value manually


# 2. Create a generator from a string "PYTHON"
# Use next() to print the first three characters


# 3. Write a generator that yields the squares of numbers in a list: [1, 2, 3, 4]
# Use a for loop to print all results


# ------------------
# yield vs return
# ------------------

# 4. Create a function that uses return to return numbers 1 and 2
# Call the function and observe the output

# 5. Create a function that uses yield to return numbers 1 and 2
# Use next() to print each value
# Observe how yield pauses execution


# ------------------
# Generator Execution Flow
# ------------------

# 6. Write a generator function that prints "Start", then yields 1,
# prints "Middle", yields 2, and prints "End", then yields 3
# Use next() step by step and observe the execution flow


# ------------------
# Loop-Based Generators
# ------------------

# 7. Create a generator function count_up_to(limit) that yields numbers from 1 to limit
# Test it with limit=5 using a for loop


# 8. Modify the above generator to count from a start value to an end value with a custom step
# Example: start=2, end=10, step=3 → Output: 2, 5, 8


# ------------------
# Generator Expressions
# ------------------

# 9. Create a generator expression that yields the squares of numbers from 1 to 5
# Print the type of the generator and all its values using a for loop


# 10. Create a generator expression that filters numbers > 10 from the list [5, 12, 17, 3]
# Print all results using a for loop


# ------------------
# Infinite Generators
# ------------------

# 11. Write a generator infinite_counter() that yields numbers starting from 1 infinitely
# Use next() to print the first 5 values


# 12. Write a generator infinite_even_numbers() that yields even numbers starting from 0
# Print the first 6 even numbers using next()


# ------------------
# Large Data & Memory Efficiency
# ------------------

# 13. Create a generator that yields lines like "Line 0", "Line 1", ..., "Line 999999"
# Print only the first 3 lines using next()


# 14. Compare memory usage between:
# - A list: [x for x in range(1_000_000)]
# - A generator: (x for x in range(1_000_000))
# Observe the difference


# ------------------
# Generator Pipelines
# ------------------

# 15. Create two generator functions:
# - multiply_by_two(numbers): yields each number multiplied by 2
# - filter_even(numbers): yields only even numbers
#
# Combine them: first multiply by 2, then filter even numbers
# Test with [1, 2, 3, 4, 5] → Output should be 2, 4, 6, 8, 10


# ------------------
# Thinking Like Python
# ------------------

# 16. Rewrite a Fibonacci generator that yields n Fibonacci numbers
# Example: n=7 → Output: 0, 1, 1, 2, 3, 5, 8


# 17. Write a generator factorial_generator(n)
# It should yield factorials from 1! up to n!
# Example: n=5 → Output: 1, 2, 6, 24, 120


# ------------------
# Advanced Control
# ------------------

# 18. Create a generator that yields the reverse of a given list
# Example: [1, 2, 3] → Output: 3, 2, 1


# 19. Write a generator repeat_value(value, times)
# It should yield the given value the specified number of times
# Example: repeat_value("A", 3) → Output: A, A, A


# 20. Create a RangeLike generator function that mimics Python's range()
# It should support start, stop, step
# Example: RangeLike(2, 10, 2) → Output: 2, 4, 6, 81
