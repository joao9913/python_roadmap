"""
03_while_loops.py
Topic: While Loops (Control Flow - Conditional Iteration)
Goal: Understand conditional iteration, loop control, sentinel values, infinite loops and common patterns
"""

# ------------------
# Basic While Loop
# ------------------

# A while loop runs as long as a condition is True

count = 0

while count < 5:
    print(count)
    count += 1

# IMPORTANT:
# You must update the variable inside the loop
# Otherwise, the loop will run forever


# ------------------
# Infinite Loop (Danger)
# ------------------

# while True:
#   print("This runs forever")

# Use carefully. Tipically controlled with break


# ------------------
# Break in While Loop
# ------------------

number = 0

while True:
    if number == 3:
        break
    print(number)
    number += 1

# Loop stops when break is executed


# ------------------
# Continue In While Loop
# ------------------

number = 0

while number < 6:
    number += 1

    if number == 3:
        continue

    print(number)

# Skips printing 3


# ------------------
# While with Else
# ------------------

# The else block runs if the loop ends normally
# (i.e., not stopped by break)

number = 0

while number < 3:
    print(number)
    number += 1
else:
    print("Loop completed")

# If break occurs, else will NOT execute


# ------------------
# Sentinel Controlled Loop
# ------------------

# A sentinel value is a special value that stops the loop

user_input = ""

while user_input != "quit":
    user_input = input("Type 'quit' to stop: ")
    print("You typed: ", user_input)

# Loop ends when user types "quit"


# ------------------
# Accumulator Pattern
# ------------------

numbers = [1, 2, 3, 4]
index = 0
total = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print("Sum: ", total)


# ------------------
# Counting Patterns
# ------------------

numbers = [1, 4, 6, 8, 3, 10]
index = 0
count_even = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        count_even += 1
    index += 1

print("Even count: ", count_even)


# ------------------
# Input Validation Pattern
# ------------------

# Keep asking until user provides valid input

user_age = -1

while user_age < 0:
    user_age = int(input("Enter a positive age: "))

print("Valid age: ", user_age)


# ------------------
# Menu Loop Pattern
# ------------------

choice = ""

while choice != "exit":
    print("1 - Say hello")
    print("2 - Say bye")
    print("Type 'exit' to quit")

    choice = input("Choose: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Bye")
    elif choice == "exit":
        print("Exiting")
    else:
        print("Invalid option")


# ------------------
# Searching With While
# ------------------

numbers = [10, 20, 30, 40, 50]
target = 30
index = 0
found = False

while index < len(numbers):
    if numbers[index] == target:
        found = True
        break
    index += 1

print("Found: ", found)


# ------------------
# When to use While vs For Loops
# ------------------

# Use for:
# - When iterating over a know iterable (list, string, range)

# While while:
# - When the number of iterations is unknown
# - When looping depends on a condition
# - When waiting for user input
# - When building interactive programs


# ------------------
# Common Mistakes
# ------------------

# 1. Forgetting to updae the loop variable (infinite loop)
# 2. Off-by-one errors in index control
# 3. Using while where for is cleaner
# 4. Not handling invalid user input safely
# 5. Creating loops that never terminate