"""
02_for_loops.py
Topic: For Loops (Control Flow - Iteration)
Goal: Understand iteration over sequences, range(), loop control and common patterns
"""


# ------------------
# Basic For Loop
# ------------------

# A for loop over each element in an iterable

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# The loop variable (number) takes each value from the list


# ------------------
# Iterating Over Strings
# ------------------

text = "Python"

for char in text:
    print(char)

# Strings are iterable.
# Each iteration gives one character


# ------------------
# Using range()
# ------------------

# range(stop)
for i in range(5):
    print(i)

# Produces: 0, 1, 2, 3, 4


# range(start, stop)
for i in range(2, 6):
    print(i)

# Produces: 2, 3, 4, 5


# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)

# Produces 0, 2, 4, 6, 8


# ------------------
# Looping With Index
# ------------------

fruits = ["apple", "banana", "cherry"]

for index in range(len(fruits)):
    print(index, fruits[index])

# Common pattern when index is required


# ------------------
# enumerate()
# ------------------

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Cleaner and more Pythonic than range(len(...))


# ------------------
# Loop Over Dictionaries
# ------------------

person = {
    "name": "Joao",
    "age": 26,
    "city": "Lisbon"
}

# Keys only
for key in person:
    print(key)

# Value only
for value in person.values():
    print(value)

# Key-value pairs
for key, value in person.items():
    print(key, value)


# ------------------
# Break Statement
# ------------------

for number in range(10):
    if number == 5:
        break
    print(number)

# Stops the loop immediately


# ------------------
# Continue Statement
# ------------------

for number in range(6):
    if number == 3:
        continue
    print(number)

# Skips current iteration only


# ------------------
# Else With For Loop
# ------------------

# The else block runs if the loop completes normally
# (i.e. not interrupted by break)

for number in range(5):
    print(number)
else:
    print("Loop completed")


# ------------------
# Nested Loops
# ------------------

for i in range(3):
    for j in range(2):
        print("i: ", i, "j: ", j)
    
# Outer loop controls rows
# Inner loop controls columns


# ------------------
# Iterating Over Sets
# ------------------

unique_numbers = {1, 2, 3, 4}

for num in unique_numbers:
    print(num)

# Order is NOT guaranteed


# ------------------
# Accumulator Pattern
# ------------------

total = 0

for number in [1, 2, 3, 4]:
    total += number

print("Sum: ", total)

# Common pattern, accumulate a result


# ------------------
# Filtering Pattern
# ------------------

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)

# Prints only even numbers


# ------------------
# Looping Over Multiple Iterables (zip)
# ------------------

names = ["Ana", "Bruno", "Carlos"]
ages = [23, 30, 19]

for name, age in zip(names, ages):
    print(name, age)

# Iterates in parallel


# ------------------
# Common Mistakes
# ------------------

# 1. Modifying a list while iterating over it (can cause logic errors)
# 2. Forgetting indentation
# 3. Confusing range(stop) with range (start, stop)
# 4. Assuming set order is predictable
# 5. Using range(len(...)) when enumerate() is cleaner