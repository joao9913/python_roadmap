"""
01_basic_functions.py
Topic: Basic Functions
Goal: Understand how to define, call and structure functions properly
"""

# ------------------
# What Is A Function?
# ------------------

# A function is a reusable block of code
# It help avoid repetition and improve structure


# ------------------
# Defining a Function
# ------------------

def greet():
    print("Hello")

# Calling the function
greet()


# ------------------
# Parameters
# ------------------

# Functions can receive input values (parameters)

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Carlos")


# ------------------
# Multiple Parameters
# ------------------

def add(a, b):
    result = a + b
    print(result)

add(5, 3)


# ------------------
# Return Values
# ------------------

# Instead of printing, functions can return values

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)


# ------------------
# Why Return Is Important
# ------------------

# Allows reuse of the value

def square(n):
    return n ** 2

value = square(6)
print(value + 10)


# ------------------
# Default Parameters
# ------------------

def greet_with_default(name = "User"):
    print(f"Hello, {name}")


greet_with_default()
greet_with_default("Ana")


# ------------------
# Keyword Arguments
# ------------------

def introduce(name, age):
    print(f"My name is {name} and i am {age} years old.")

introduce(age=30, name="Miguel")


# ------------------
# Positional vs Keyword Arguments
# ------------------

# Positional (order matters)
introduce("Sara", 25)

# Keyword (order does not matter)
introduce(age=25, name = "Sara")


# ------------------
# Returning Multiple Values
# ------------------

def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)


# ------------------
# Function Scope (Local Variables)
# ------------------

def example():
    local_variable = 10
    print(local_variable)

example()

# print(local_variable) # This would cause an error


# ------------------
# Global Variables
# ------------------

global_var = 100

def show_global():
    print(global_var)

show_global()


# ------------------
# Function Calling Another Function
# ------------------

def double(n):
    return n * 2

def process_number(n):
    doubled = double(n)
    return doubled + 5

print(process_number(10))


# ------------------
# Docstrings
# ------------------

def subtract(a, b):
    """
    Subtracts b from a and returns the result
    """
    return a - b

print(subtract(10, 3))