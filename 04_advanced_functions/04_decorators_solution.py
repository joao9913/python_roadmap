# ------------------
# Functions As Objects
# ------------------

# 1. Create a function say_hello that prints "Hello".
# Assign the function to a variable called greet.
# Call greet().

print("#1")

def say_hello():
    print("Hello")

greet = say_hello
greet()

print()


# 2. Create a function run_function(func)
# It should call the function passed as an argument.
# Pass say_hello to it.

print("#2")

def run_function(func):
    func()

run_function(say_hello)

print()

# ------------------
# Returning Functions
# ------------------

# 3. Create a function outer() that defines another function inner()
# inner() should print "Inner function running".
# outer() should return inner.
# Store the returned function and call it.

print("#3")

def outer():
    def inner():
        print("Inner function running")

    return inner

def_result = outer()
def_result()

print()

# ------------------
# Simple Decorators
# ------------------

# 4. Create a decorator called simple_decorator.
# It should:
# - print "Before function"
# - run the function
# - print "After function"

print("#4")

def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

print()

# 5. Apply the decorator manually to a function greet()
# Then call the decorated version.

print("#5")

def greet():
    print("Hello")

decorated = simple_decorator(greet)
decorated()

print()

# ------------------
# Decorator Syntax
# ------------------

# 6. Use the @simple_decorator syntax on a function say_hi()
# The function should print "Hi!".

print("#6")

@simple_decorator
def say_hi():
    print("Hi!")

say_hi()

print()

# ------------------
# Decorators With Arguments
# ------------------

# 7. Create a decorator log_call that prints:
# "Calling function..." before executing the function.

print("#7")

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper

print()

# 8. Apply log_call to a function greet_person(name)
# The function should print "Hello <name>".

print("#8")

@log_call
def greet_person(name):
    print(f"Hello {name}")

print()

greet_person("Joao")

# ------------------
# Returning Values
# ------------------

# 9. Create a decorator called double_result.
# It should double the return value of the function.

print("#9")

def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

print()

# 10. Apply double_result to a function add(a, b)
# The function should return a + b.

print("#10")

@double_result
def add(a, b):
    return a + b

print(add(1, 2))

print()

# ------------------
# Multiple Decorators
# ------------------

# 11. Create two decorators:
# decorator_one → prints "Decorator One"
# decorator_two → prints "Decorator Two"

print("#11")

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper

print()


# 12. Apply both decorators to a function message()
# Print "Hello from function".
# Observe the order they execute.

print("#12")

@decorator_one
@decorator_two
def message():
    print("Hello from function")

message()

print()


# ------------------
# Decorators With Parameters
# ------------------

# 13. Create a decorator repeat(n)
# It should run the decorated function n times.

print("#13")

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

print()


# 14. Apply repeat(3) to a function say_hello()
# The function should print "Hello!".

print("#14")

import time

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

print()

# ------------------
# Practical Decorators
# ------------------

# 15. Create a decorator timer
# It should measure execution time of the function.

print("#15")

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Took {end - start:.6f} seconds to run")
        return result
    return wrapper

print()

# 16. Apply timer to a function slow_function()
# Make the function sleep for 1 second.

print("#16")

@timer
def slow_function():
    time.sleep(1)

slow_function()

print()

# ------------------
# Logging Decorator
# ------------------

# 17. Create a decorator logger
# It should print the function name before running it.

print("#17")

def logger(func):
    def wrapper():
        print(f"Function is called {func.__name__}")
        return func()
    return wrapper

@logger
def function1():
    print("Running function1")

function1()

print()


# ------------------
# Access Control Decorator
# ------------------

# 18. Create a decorator require_admin
# It should only run the function if user == "admin"
# Otherwise print "Access denied".

print("#18")

def require_admin(func):
    def wrapper(*args, **kwargs):
        if args[0] == "admin":
            func(*args, **kwargs)
        else:
            print("Access denied")
    return wrapper

@require_admin
def delete_account(user):
    print("Account delete")

delete_account("joao")

print()

# ------------------
# Caching (Memoization)
# ------------------

# 19. Create a decorator cache
# Store results of function calls in a dictionary
# If the function is called again with the same arguments,
# return the stored result.

print("#19")

def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache_dict:
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper

@cache
def create_user(name, age):
    print(f"Created user {name}, who is {age} years old")

create_user("Joao", 26)
create_user("Ana", 36)
create_user("Joao", 26)

print()


# ------------------
# Advanced Challenge
# ------------------

# 20. Create a decorator validate_positive
# It should raise a ValueError if any argument is negative.

print("#20")

def validate_positive(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if value < 0:
                raise ValueError

        for value in kwargs.values():
            if value < 0:
                raise ValueError

        func(*args, **kwargs)
    return wrapper

@validate_positive
def print_numbers(a, b):
    print(f"Numbers: {a}, {b}")

print_numbers(1, 2)
print_numbers(1, 2)

print()
