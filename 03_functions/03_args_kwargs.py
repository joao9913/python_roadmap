"""
03_args_kwargs.py
Topic: *args and **kwargs
Goal: Understand how to accept flexible numbers of arguments in functions
"""


# ------------------
# Why *args and **kwargs Exist
# ------------------

# Normally, functions require a fixed number of parameters.
# But sometimes, we want functions that accept:
# - any number of positional arguments
# - any number of keyword arguments

# Python provides:
# *args -> multiple positional arguments
# **kwargs -> multiple keyword arguments


# ------------------
# *args (Variable Positional Arguments)
# ------------------

# *args allows a function to accept any number of positional arguments
# Inside the function, args becomes a tuple

def add_numbers(*args):
    print(args)

add_numbers(1, 2, 3)
add_numbers(10, 20, 30, 40)


# ------------------
# Using *args in Loops
# ------------------

# Because args is a tuple, we can iterate over it

def sum_numbers(*args):
    total = 0

    for number in args:
        total += number

    print("Sum: ", total)

sum_numbers(1, 2, 3)
sum_numbers(5, 10, 15, 20)


# ------------------
# Mixing Normal Parameters and *args
# ------------------

def introduce(person, *hobbies):
    print("Name: ", person)

    for hobby in hobbies:
        print("Hobby: ", hobby)
    
introduce("Ana", "Reading", "Swimming", "Gaming")


# ------------------
# ** kwargs (Variable Keyword Arguments)
# ------------------

# **kwargs allows passing named arguments
# Inside the function, kwargs becomes a dictionary

def show_profile(**kwargs):
    print(kwargs)

show_profile(name="Ana", age=25, country="Portugal")


# ------------------
# Iterating Through **kwargs
# ------------------

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_user_info(name="Carlos", age=30, city="Lisbon")


# ------------------
# Mixing Parameters, *args and **kwargs
# ------------------

# Order matters when combining parameters

# Correct order:
# 1. Normal parameters
# 2. *args
# 3. **kwargs

def example(a, b, *args, **kwargs):
    print("a: ", a)
    print("b: ", b)

    print("args: ", args)
    print("kwargs: ", kwargs)

example(
    10,
    20,
    30,
    40,
    50,
    name="Ana",
    role="Admin"
)


# ------------------
# Unpacking Arguments
# ------------------

# We can also unpack lists or dictionaries when calling functions

def multiply(a, b, c):
    print(a * b * c)

numbers = [2, 3, 4]
multiply(*numbers)

def print_person(name, age, country):
    print(name, age, country)

person = {
    "name": "Joao",
    "age": 26,
    "country": "Portugal"
}

print_person(**person)


# ------------------
# Real World Example
# ------------------

# A logging function that accepts flexible parameters

def log_message(level, *messages, **metadata):
    print("Level: ", level)

    for msg in messages:
        print("Message: ", msg)
    
    for key, value in metadata.items():
        print(key, ":", value)
    
log_message(
    "INFO",
    "User logged in",
    "Session started",
    user = "admin",
    ip = "192,168.1.1"
)