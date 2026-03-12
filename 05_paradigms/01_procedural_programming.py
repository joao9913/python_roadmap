"""
01_procedural_programming.py
Topic: Procedural Programming
Goal: Understand the basics of procedural programming in Python and how to structure programs using functions and procedures.
"""

# ------------------
# What Is Procedural Programming
# ------------------

# Procedural programming is a programming paradigm based on the concept of
# procedures (also called routines, subroutines or functions)
# Programs are organized as a sequence of steps and procedures

# Key concepts:
# - Sequence: Code executes line by line
# - Procedures/Functions: reusable blocks of code
# - Modularity: Breaking tasks into functions
# - Global vs Local variables


# ------------------
# Example: Sequential Execution
# ------------------

print("Step 1: Start program")
print("Step 2: Do something")
print("Step 3: End program")


# ------------------
# Example: Using Functions
# ------------------

def greet_user(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

greet_user("Joao")
result = add_numbers(1, 5)
print("Result is: ", result)


# ------------------
# Modular Programs
# ------------------

# You can organize your program into smaller reusable functions

def get_input():
    return int(input("Enter a number: "))

def square_number(n):
    return n ** 2

def main():
    number = get_input()
    squared = square_number(number)
    print("Squared: ", squared)

main()


# ------------------
# Global vs Local Variables
# ------------------

x = 10  # Global variable

def modify_x():
    global x
    x += 5
    print("Inside function, x = ", 5)

modify_x()
print("Outside function, x = ", x)


# ------------------
# When to Use Procedural Programming
# ------------------

# - Small scripts
# - Step-by-step processes
# - Calculations
# - Situations where OOP or functional programming is not needed


# ------------------
# Summary
# ------------------

# Procedural programming:
# - Organizes code using functions
# - Uses sequence, loops and conditionals
# - Focuses on tasks and procedures rather than objects
