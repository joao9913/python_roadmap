# -------------------------------------------------
# 1. Basic Abstract Class
# -------------------------------------------------

# Create an abstract class Shape with an abstract method area()
# Then create a subclass Circle that implements area()


# -------------------------------------------------
# 2. Multiple Abstract Methods
# -------------------------------------------------

# Create an abstract class Vehicle with:
# - abstract method start_engine()
# - abstract method stop_engine()
# Then create a subclass Car implementing both methods


# -------------------------------------------------
# 3. Abstract Method with Default Behavior
# -------------------------------------------------

# Create an abstract class Animal with abstract method speak()
# Give speak() a default print("Some generic sound")
# Create subclass Dog that calls super().speak() and then prints "Woof!"


# -------------------------------------------------
# 4. Prevent Instantiation
# -------------------------------------------------

# Try to create an instance of an abstract class directly
# Observe the error


# -------------------------------------------------
# 5. Polymorphism with Abstract Classes
# -------------------------------------------------

# Create an abstract class Payment with abstract method pay()
# Create subclasses CreditCardPayment and PayPalPayment
# Store them in a list and call pay() on each


# -------------------------------------------------
# 6. Abstract Class with Constructor
# -------------------------------------------------

# Create an abstract class Employee with:
# - __init__(name)
# - abstract method calculate_pay()
# Subclass Manager that implements calculate_pay()


# -------------------------------------------------
# 7. Nested Abstract Classes
# -------------------------------------------------

# Create abstract class Logger with abstract method log()
# Create abstract class FileLogger(Logger)
# Create subclass TextLogger implementing log()


# -------------------------------------------------
# 8. Enforcing Interfaces
# -------------------------------------------------

# Create abstract class Database with abstract method connect()
# Create subclass MySQLDatabase implementing connect()
# Demonstrate that another subclass without connect() cannot be instantiated


# -------------------------------------------------
# 9. Abstract Properties
# -------------------------------------------------

# Create abstract class Product with abstract property price
# Subclass Book implementing price as a property


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create abstract class Strategy with abstract method execute()
# Implement 3 different trading strategies as subclasses
# Store them in a list and call execute() on each
