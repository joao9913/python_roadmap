"""
04_decorators.py
Topic: Decorators
Goal: Understand how decorators work and how they mnodify functions without changing their code.
"""

# ------------------
# Functions Are Objects
# ------------------

# In Python, functions are first-class objects
# This means they can be:
# - assigned to variables
# - passed as arguments
# - returned from other functions

def say_hello():
    print("Hello")

func = say_hello
func()


# ------------------
# Passing Functions As Arguments
# ------------------

def greet(func):
    print("Before greeting")
    func()
    print("After greeting")

def say_hi():
    print("Hi!")

greet(say_hi)


# ------------------
# Returning Functions
# ------------------

# A function can return another function

def outer():
    def inner():
        print("Inner function")

    return inner

returned_func = outer()
returned_func()


# ------------------
# Creating A Simple Decorator
# ------------------

# A decorator wraps another function and modifies its behaviour

def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

def greet_user():
    print("Hello user")

decorated = simple_decorator(greet_user)
decorated()


# ------------------
# Decorator Syntax
# ------------------

# Python provides the @ syntax to apply decorators

@simple_decorator
def greet_again():
    print("Hello again")

greet_again()


# ------------------
# Decorators With Arguments
# ------------------

# If the decorated function takes arguments,
# the wrapper must also accept them

def decorator_args(func):
    def wrapper(*args, **kwargs):
        print("Function starting")
        func(*args, **kwargs)
        print("Function finished")
    return wrapper

@decorator_args
def greet_person(name):
    print(f"Hello {name}")

greet_person("Joao")


# ------------------
# Returning Values From Decorators
# ------------------

def decorator_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_return
def add(a, b):
    return a + b

print(add(3, 5))


# ------------------
# Multiple Decorators
# ------------------

def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator one")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def message():
    print("Hello")

message()


# ------------------
# Decorators With Parameters
# ------------------

# A decorator can also accept its own arguments

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()


# ------------------
# Pratical Example: Timing Functions
# ------------------
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()


# ------------------
# When Decorators Are Useful
# ------------------

# Common real-world uses:

# Logging
# Authentication
# Caching
# Timing
# Input Validation
# Access Control


# ------------------
# Summary
# ------------------

# Decorators wrap functions to modify behaviour
# Functions are first-class objects in Python
# Decorats returna new function (wrapper)
# @ syntax is shorthand for applying decorators
# Decorators can handle arguments and return values
# Decorators can also take parameters
