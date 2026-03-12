# ------------------
# Functions As Objects
# ------------------

# 1. Create a function say_hello that prints "Hello".
# Assign the function to a variable called greet.
# Call greet().


# 2. Create a function run_function(func)
# It should call the function passed as an argument.
# Pass say_hello to it.


# ------------------
# Returning Functions
# ------------------

# 3. Create a function outer() that defines another function inner()
# inner() should print "Inner function running".
# outer() should return inner.
# Store the returned function and call it.


# ------------------
# Simple Decorators
# ------------------

# 4. Create a decorator called simple_decorator.
# It should:
# - print "Before function"
# - run the function
# - print "After function"


# 5. Apply the decorator manually to a function greet()
# Then call the decorated version.


# ------------------
# Decorator Syntax
# ------------------

# 6. Use the @simple_decorator syntax on a function say_hi()
# The function should print "Hi!".


# ------------------
# Decorators With Arguments
# ------------------

# 7. Create a decorator log_call that prints:
# "Calling function..." before executing the function.


# 8. Apply log_call to a function greet_person(name)
# The function should print "Hello <name>".


# ------------------
# Returning Values
# ------------------

# 9. Create a decorator called double_result.
# It should double the return value of the function.


# 10. Apply double_result to a function add(a, b)
# The function should return a + b.


# ------------------
# Multiple Decorators
# ------------------

# 11. Create two decorators:
# decorator_one → prints "Decorator One"
# decorator_two → prints "Decorator Two"


# 12. Apply both decorators to a function message()
# Print "Hello from function".
# Observe the order they execute.


# ------------------
# Decorators With Parameters
# ------------------

# 13. Create a decorator repeat(n)
# It should run the decorated function n times.


# 14. Apply repeat(3) to a function say_hello()
# The function should print "Hello!".


# ------------------
# Practical Decorators
# ------------------

# 15. Create a decorator timer
# It should measure execution time of the function.


# 16. Apply timer to a function slow_function()
# Make the function sleep for 1 second.


# ------------------
# Logging Decorator
# ------------------

# 17. Create a decorator logger
# It should print the function name before running it.


# ------------------
# Access Control Decorator
# ------------------

# 18. Create a decorator require_admin
# It should only run the function if user == "admin"
# Otherwise print "Access denied".


# ------------------
# Caching (Memoization)
# ------------------

# 19. Create a decorator cache
# Store results of function calls in a dictionary
# If the function is called again with the same arguments,
# return the stored result.


# ------------------
# Advanced Challenge
# ------------------

# 20. Create a decorator validate_positive
# It should raise a ValueError if any argument is negative.
