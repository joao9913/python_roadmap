"""
02_scope.py
Topic: Variable Scope
Goal: Understand how variables nehave inside and outside functions
"""


# ------------------
# What Is Scope?
# ------------------

# Scope defines where a variable can be accessed in a program
# A variable created inside a function is not accessible outside of it


# ------------------
# Local Scope
# ------------------

# Variables defined inside a function are local to that function.

def my_function():
    x = 10
    print("Inside function: ", x)

my_function()

# print(x)  # this would cause an error because x only exists inside the function


# ------------------
# Global Scope
# ------------------

# Variables defined outside functions are global

x = 20

def show_global():
    print("Global x: ", x)

show_global()
print("Outside function: ", x)


# ------------------
# Local vs Global Variables
# ------------------

# A local variable with the same name will override the global variable inside the function

x = 50

def test_scope():
    x = 10
    print("Inside function: ", x)

test_scope()
print("Outside functin: ", x)


# ------------------
# Modifying Global Variables
# ------------------

# To modify a global variable inside a function,
# Python requires the global keyword

count = 0

def increase():
    global count
    count += 1

increase()
increase()

print("Count: ", count)


# ------------------
# Nested Scope
# ------------------

# Functions inside functions create another level of scope.

def outer_function():
    outer_var = "I am outside"

    def inner_function():
        print(outer_var)
    
    inner_function()

outer_function()


# ------------------
# LEGB Rule (Concept)
# ------------------

# Python searches variables in this order:
# L - Local
# E - Enclosing
# G - Global
# B - Built-In

x = 5

def example():
    x = 10
    print(x)

example()
print(x)