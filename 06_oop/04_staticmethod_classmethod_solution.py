# ------------------
# Static Utility
# ------------------

# 1. Create a class called NumberUtils.
#
# Add a static method called is_even(number)
# that returns True if the number is even and False otherwise.
#
# Call the method using the class.

#print("\n#1")

class NumberUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(NumberUtils.is_even(7))


# ------------------
# Static Calculation
# ------------------

# 2. Create a class called GeometryUtils.
#
# Add a static method called circle_area(radius)
# that returns the area of a circle.
#
# Do not store any object state.

print("\n#2")

import math

class GeometryUtils:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

print(GeometryUtils.circle_area(2))

# ------------------
# Static Validation
# ------------------

# 3. Create a class called EmailValidator.
#
# Add a static method called is_valid(email)
# that returns True if the email contains "@" and ".".
#
# This method should not rely on instance or class data.

print("\n#3")

class EmailValidator:
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email

print(EmailValidator.is_valid("email@gmail.com"))


# ------------------
# Class Method Reading Class Data
# ------------------

# 4. Create a class called AppConfig.
#
# Add a class variable:
# - version = "1.0"
#
# Add a class method get_version()
# that returns the current version.

print("\n#4")

class AppConfig:
    version = "1.0"

    @classmethod
    def get_version(cls):
        return cls.version

print(AppConfig.get_version())

# ------------------
# Class Counter
# ------------------

# 5. Create a class called Session.
#
# Add a class variable called active_sessions.
#
# Each time a new Session object is created,
# increase the counter.
#
# Add a class method get_active_sessions()
# that returns the total.

print("\n#5")

class Session:
    active_sessions = 0

    def __init__(self):
        Session.active_sessions += 1

    @classmethod
    def get_active_sessions(cls):
        return cls.active_sessions

session1 = Session()
print(Session.get_active_sessions())

session2 = Session()
print(Session.get_active_sessions())


# ------------------
# Factory Class Method
# ------------------

# 6. Create a class called User.
#
# Instance attributes:
# - username
#
# Create a class method called guest_user()
# that returns a User object with username = "Guest".

print("\n#6")

class User:
    username = "Guest"

    def __init__(self, name):
        self.username = name

    @classmethod
    def guest_user(cls):
        return cls("Guest")

user = User("user")
print(user.username)
print(User.guest_user())


# ------------------
# Alternative Constructor
# ------------------

# 7. Create a class called Temperature.
#
# Instance attribute:
# - celsius
#
# Add a class method from_fahrenheit(f)
# that converts Fahrenheit to Celsius and
# returns a Temperature object.

print("\n#7")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5 / 9
        return cls(celsius)

temp_f = Temperature.from_fahrenheit(32)
print(temp_f.celsius)

temp_c = Temperature(25)
print(temp_c.celsius)


# ------------------
# Static Helper Inside a Class
# ------------------

# 8. Create a class called PasswordUtils.
#
# Add a static method called is_strong(password)
# that returns True if:
# - length >= 8
# - contains at least one number
#
# No instance or class variables should be used.

print("\n#8")

class PasswordUtils:
    @staticmethod
    def is_strong(password):
        return len(password) >= 8 and any(char.isdigit() for char in password)

print(PasswordUtils.is_strong("ooooooooooo"))

# ------------------
# Instance + Class Interaction
# ------------------

# 9. Create a class called Product.
#
# Instance attributes:
# - name
# - price
#
# Class variable:
# - tax_rate = 0.2
#
# Add:
# - an instance method final_price() that includes tax
# - a class method set_tax_rate(new_rate)

print("\n#9")

class Product:
    tax_rate = 0.2

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price * (1 + self.tax_rate)

    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

product = Product("name", 10)
print(product.final_price())

Product.set_tax_rate(0.3)
print(product.final_price())


# ------------------
# Class Method as Object Builder
# ------------------

# 10. Create a class called Coordinate.
#
# Instance attributes:
# - x
# - y
#
# Add a class method from_tuple(data)
# where data is a tuple like (x, y).
#
# The method should return a Coordinate object.

print("\n#10")

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, data):
        x = data[0]
        y = data[1]
        return cls(x, y)

tuple_example = (10, 5)
coordinates = Coordinate.from_tuple(tuple_example)
print(coordinates.x, coordinates.y)


# ------------------
# Static Method for Comparison
# ------------------

# 11. Create a class called ScoreUtils.
#
# Add a static method higher_score(a, b)
# that returns the larger value.

print("\n#11")

class ScoreUtils:
    @staticmethod
    def higher_score(a, b):
        return a if a > b else b

print(ScoreUtils.higher_score(10, 50))


# ------------------
# Static Method for Data Transformation
# ------------------

# 12. Create a class called TextFormatter.
#
# Add a static method normalize(text)
# that:
# - removes leading/trailing spaces
# - converts the text to lowercase.

print("\n#12")

class TextFormatter:
    @staticmethod
    def normalize(text):
        normalized_text = text.lower().strip()

        return normalized_text

print(TextFormatter.normalize("   PyTHOn   "))


# ------------------
# Class-Level Limits
# ------------------

# 13. Create a class called ApiClient.
#
# Class variable:
# - request_limit = 100
#
# Add a class method set_limit(new_limit)
# to update the limit.
#
# Add another class method get_limit().

print("\n#13")

class ApiClient:
    request_limit = 100

    @classmethod
    def set_limit(cls, new_limit):
        cls.request_limit = new_limit

    @classmethod
    def get_limit(cls):
        return cls.request_limit

print(ApiClient.get_limit())
ApiClient.set_limit(200)
print(ApiClient.get_limit())


# ------------------
# Class Method Tracking Instances
# ------------------

# 14. Create a class called Worker.
#
# Class variable:
# - worker_count
#
# Increase it every time a Worker object is created.
#
# Add a class method total_workers().

print("\n#14")

class Worker:
    worker_count = 0

    def __init__(self):
        Worker.worker_count += 1

    @classmethod
    def total_workers(cls):
        return cls.worker_count

worker1 = Worker()
print(Worker.total_workers())
worker2 = Worker()
print(Worker.total_workers())


# ------------------
# Static Method for Input Checking
# ------------------

# 15. Create a class called AgeChecker.
#
# Add a static method is_adult(age)
# that returns True if age >= 18.

print("\n#15")

class AgeChecker:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(AgeChecker.is_adult(17))


# ------------------
# Factory with Multiple Parameters
# ------------------

# 16. Create a class called Rectangle.
#
# Instance attributes:
# - width
# - height
#
# Add a class method square(size)
# that creates a rectangle where width and height are equal.

print("\n#16")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)

rect = Rectangle.square(10)
print(rect.height, rect.width)


# ------------------
# Concept Review
# ------------------

# 17. In comments, explain:
#
# - When should you use a static method?
# - When should you use a class method?
# - What does "cls" represent?
# - Why are class methods often used as factory methods?
# - Why shouldn't static methods depend on instance data?

print("\n#17")

# When you want methods that have no actual relation to the class. Useful for utils for example
# When you want some sort of secondary constructor, or a method that changes or returns a class variable
# cls represents the class
# Because they can be used as a secondary constructor
# Because they do not interact with the objects
