# -------------------------------------------------
# 1. Basic Inheritance
# -------------------------------------------------

# Create a class called Person.
#
# Instance attributes:
# - name
#
# Create a class called Employee that inherits from Person.
#
# Employee should have:
# - salary
#
# Create an Employee object and access both attributes.


# -------------------------------------------------
# 2. Method Overriding
# -------------------------------------------------

# Create a class called Shape.
#
# Add a method:
# - area() that returns 0
#
# Create a class called Square that inherits from Shape.
#
# Square should:
# - have attribute side
# - override area() to return the correct value


# -------------------------------------------------
# 3. Using super()
# -------------------------------------------------

# Create a class called Animal.
#
# It should have:
# - name
#
# Create a class called Bird that inherits from Animal.
#
# Bird should:
# - add attribute can_fly
# - use super() in __init__


# -------------------------------------------------
# 4. Extending Parent Behavior
# -------------------------------------------------

# Create a class called Message.
#
# It should have:
# - content
#
# Add method:
# - display() that returns content
#
# Create a class called EncryptedMessage that inherits from Message.
#
# Override display() so it:
# - modifies the content before returning it
# - but still uses super()


# -------------------------------------------------
# 5. isinstance() and issubclass()
# -------------------------------------------------

# Create:
# - Base class Vehicle
# - Child class Bike

# Write code that:
# - Checks if an object is instance of Vehicle
# - Checks if Bike is a subclass of Vehicle


# -------------------------------------------------
# 6. Constructor Inheritance
# -------------------------------------------------

# Create a class called User.
#
# It should have:
# - username
#
# Create a class called Admin that inherits from User.
#
# Admin should:
# - have attribute permissions
# - correctly call parent constructor


# -------------------------------------------------
# 7. Multi-Level Inheritance
# -------------------------------------------------

# Create:
# - Class A
# - Class B that inherits from A
# - Class C that inherits from B
#
# Add a method in A.
# Call it from an instance of C.


# -------------------------------------------------
# 8. Method Resolution Order (MRO)
# -------------------------------------------------

# Create two parent classes:
# - Class X with method show()
# - Class Y with method show()
#
# Create class Z that inherits from X and Y.
#
# Observe which method is called.
# Print the MRO of class Z.


# -------------------------------------------------
# 9. Polymorphism
# -------------------------------------------------

# Create:
# - Class Dog with method speak()
# - Class Cat with method speak()
#
# Write code that:
# - Stores both in a list
# - Iterates through them
# - Calls speak() on each
# (Demonstrate polymorphism)


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a base class Account.
#
# It should have:
# - balance
#
# Create:
# - SavingsAccount (adds interest_rate)
# - CheckingAccount (adds transaction_fee)
#
# Each subclass should:
# - Extend behavior appropriately
# - Use super() where necessary
