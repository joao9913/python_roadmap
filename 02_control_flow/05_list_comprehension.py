"""
05_list_comprehensions.py
Topic: List Comprehensions
Goal: Learn how to create lists efficiently using concise expressions
"""


# ------------------
# Basic List Comprehension
# ------------------

# Traditional way
numbers = []
for i in range(5):
    numbers.append(i)

# List comprehension version
numbers_comp = [i for i in range(5)]


# ------------------
# Expression Before the Loop
# ------------------

# Square numbers from 0 to 4
squares = [i ** 2 for i in range(5)]

# Convert numbers to strings
strings = [str(i) for i in range(5)]


# ------------------
# With Condition (Filtering)
# ------------------

# Get only even numbers
evens = [i for i in range(10) if i % 2 == 0]

# Get numbers greater than 5
greater_than_five = [i for i in range(10) if i > 5]


# ------------------
# If-Else Expression Inside
# ------------------

# Label numbers as even or odd
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(6)]


# ------------------
# Using Existing Lists
# ------------------

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = [i * 2 for i in numbers]

# Keep only numbers > 2
filtered = [n for n in numbers if n > 2]


# ------------------
# Nested List Comprehension
# ------------------

# Flatten a matrix
matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]


# ------------------
# Nested Loops (Cartesian Product)
# ------------------

pairs = [(x, y) for x in range(3) for y in range(2)]


# ------------------
# Multiple Conditions
# ------------------

numbers = range(20)

#Even numbers divisible by 4
filtered_numbers = [n for n in numbers if n % 2 == 0 and n % 4 == 0]


# ------------------
# List Comprehension vs map()
# ------------------

# Using map()
squared_map = list(map(lambda x: x ** 2, range(5)))

# Using list comprehension (more readable)
squared_comp = [x ** 2 for x in range(5)]


# ------------------
# List Comprehension vs filter()
# ------------------

# Using filter()
evens_filter = list(filter(lambda x: x % 2 == 0, range(10)))

# Using list comprehension (clearer)
evens_comp = [x for x in range(10) if x % 2 == 0]


# ------------------
# Set and Dictionary Comprehensions (Preview)
# ------------------

# Set comprehension
unique_squares = {x ** 2 for x in range(5)}

# Dictionary comprehension
square_dict = {x: x ** 2 for x in range(5)}