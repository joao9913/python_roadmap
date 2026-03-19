# 08_polymorphism_exercises.py
# Topic: Polymorphism
# Goal: Practice using shared interfaces, duck typing, and method overriding

print("\n# Polymorphism Exercises\n")

# -------------------------------------------------
# 1. Basic Polymorphism
# -------------------------------------------------

# Create two classes:
# - Dog
# - Cat
#
# Both should have:
# - method speak()
#
# Create objects and call speak() on both.


# -------------------------------------------------
# 2. Polymorphism with Lists
# -------------------------------------------------

# Create:
# - Dog
# - Cat
# - Bird
#
# Each should implement:
# - speak()
#
# Store them in a list and:
# - iterate through the list
# - call speak() on each


# -------------------------------------------------
# 3. Duck Typing (No Inheritance)
# -------------------------------------------------

# Create:
# - Class Robot with method speak()
# - Class Human with method speak()
#
# Write a function:
# - make_sound(obj)
#   that calls obj.speak()
#
# Pass different objects to the function.


# -------------------------------------------------
# 4. Polymorphism with Inheritance
# -------------------------------------------------

# Create a base class Animal:
# - method speak() returns "Some sound"
#
# Create:
# - Dog (returns "Woof")
# - Cat (returns "Meow")
#
# Store them in a list and call speak().


# -------------------------------------------------
# 5. Function Polymorphism
# -------------------------------------------------

# Write a function:
# - process(obj)
#
# It should:
# - call obj.run()
#
# Create at least two classes that implement run()
# with different behaviors.


# -------------------------------------------------
# 6. Operator Polymorphism
# -------------------------------------------------

# Create a class Vector:
# - attributes: x, y
#
# Implement:
# - __add__ so two vectors can be added
#
# Test:
# v1 + v2


# -------------------------------------------------
# 7. Mixed Types (Duck Typing Failure)
# -------------------------------------------------

# Create:
# - Class Dog with speak()
# - Class Car WITHOUT speak()
#
# Put both in a list and try:
# - calling speak() on each
#
# Observe what happens.


# -------------------------------------------------
# 8. Polymorphism in Functions
# -------------------------------------------------

# Create a function:
# - describe(obj)
#
# It should:
# - call obj.describe()
#
# Create multiple classes with describe() implemented differently.


# -------------------------------------------------
# 9. Real-World Simulation
# -------------------------------------------------

# Create:
# - Class CreditCardPayment with method pay()
# - Class PayPalPayment with method pay()
# - Class CryptoPayment with method pay()
#
# Store them in a list and:
# - call pay() on each
#
# (Simulate different payment systems)


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a system where:
# - Multiple classes represent different trading strategies
#
# Each should implement:
# - execute_trade()
#
# Create at least 3 strategies and:
# - store them in a list
# - execute them in a loop
#
# Focus on:
# - same interface
# - different behavior
