# ------------------
# Basic Property (Read)
# ------------------

# 1. Create a class called User.
#
# Instance attribute:
# - _username
#
# Add a property username that returns the value.

print("\n#1")

class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

user = User("Admin")
print(user.username)


# ------------------
# Property with Validation (Write)
# ------------------

# 2. Create a class called Product.
#
# Instance attribute:
# - _price
#
# Add:
# - a property price
# - a setter that only allows values >= 0

print("\n#2")

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError

product = Product(109)
print(product.price)
product.price = 200
print(product.price)



# ------------------
# Prevent Invalid State
# ------------------

# 3. Create a class called BankAccount.
#
# Instance attribute:
# - _balance
#
# Add:
# - a property balance
# - a setter that prevents negative values

print("\n#3")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            raise ValueError

account = BankAccount(1000)
print(account.balance)
account.balance = 200
print(account.balance)


# ------------------
# Read-Only Property
# ------------------

# 4. Create a class called Circle.
#
# Instance attribute:
# - _radius
#
# Add a read-only property area that calculates:
# π * radius^2
#
# Do NOT allow setting area.

print("\n#4")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(2)
print(circle.area)


# ------------------
# Property Depending on Multiple Attributes
# ------------------

# 5. Create a class called Rectangle.
#
# Instance attributes:
# - _width
# - _height
#
# Add a property area that returns width * height.

print("\n#5")

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 10)
print(rect.area)


# ------------------
# Validation with Multiple Conditions
# ------------------

# 6. Create a class called Person.
#
# Instance attribute:
# - _age
#
# Add:
# - a property age
# - a setter that only allows:
#     age >= 0
#     age <= 120

print("\n#6")

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0 and new_age <= 120:
            self._age = new_age
        else:
            raise ValueError

person = Person(25)
print(person.age)

person.age = 30
print(person.age)


# ------------------
# Derived Property
# ------------------

# 7. Create a class called Employee.
#
# Instance attributes:
# - _salary
#
# Add:
# - a property yearly_salary (salary * 12)
# - no setter for yearly_salary

print("\n#7")

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def yearly_salary(self):
        return self._salary * 12

employee = Employee(1000)
print(employee.yearly_salary)


# ------------------
# Controlled Update
# ------------------

# 8. Create a class called Temperature.
#
# Instance attribute:
# - _celsius
#
# Add:
# - a property celsius
# - a setter that prevents values below -273.15

print("\n#8")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        if celsius >= -273.15:
            self._celsius = celsius
        else:
            raise ValueError

temp = Temperature(25)
print(temp.celsius)

temp.celsius = -123
print(temp.celsius)


# ------------------
# Multiple Properties
# ------------------

# 9. Create a class called Box.
#
# Instance attributes:
# - _width
# - _height
#
# Add:
# - property width (with validation > 0)
# - property height (with validation > 0)
# - property area (read-only)

print("\n#9")

class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._height * self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError

box = Box(10, 20)
print(box.width)
print(box.height)
print(box.area)


# ------------------
# Property with Transformation
# ------------------

# 10. Create a class called Text.
#
# Instance attribute:
# - _content
#
# Add:
# - a property content (returns original)
# - a property normalized (returns lowercase + stripped text)

print("\n#10")

class Text:
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content

    @property
    def normalized(self):
        return self._content.lower().strip()

text = Text("  Python  ")
print(text.content)
print(text.normalized)


# ------------------
# Write-Only Behavior Simulation
# ------------------

# 11. Create a class called Password.
#
# Instance attribute:
# - _password
#
# Add:
# - a setter for password that:
#     - requires length >= 8
# - a getter that raises an exception or prevents reading

print("\n#11")

class Password:
    def __init__(self, new_password):
        self.password = new_password

    @property
    def password(self):
        raise PermissionError

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 8:
            self._password = new_password
        else:
            raise ValueError

password = Password("asdasaa678")
# print(password.password)


# ------------------
# Property Triggering Logic
# ------------------

# 12. Create a class called LightSwitch.
#
# Instance attribute:
# - _is_on (boolean)
#
# Add:
# - a property is_on
# - a setter that only accepts True/False

print("\n#12")

class LightSwitch:
    def __init__(self, state):
        self.is_on = state

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, state):
        if isinstance(state, bool):
            self._is_on = state
        else:
            raise ValueError

ls = LightSwitch(True)
print(ls.is_on)


# ------------------
# Encapsulation with Internal Method Use
# ------------------

# 13. Create a class called Score.
#
# Instance attribute:
# - _value
#
# Add:
# - a property value
# - a setter that prevents values < 0
# - a method add(points) that updates value safely

print("\n#13")

class Score:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError

    def add(self, points):
        if points >= 0:
            self.value += points
        else:
            raise ValueError

score = Score(109)
print(score.value)
score.add(10)
print(score.value)


# ------------------
# Property + Class Interaction
# ------------------

# 14. Create a class called ApiClient.
#
# Instance attribute:
# - _requests_made
#
# Class variable:
# - max_requests = 100
#
# Add:
# - property requests_made
# - setter that prevents exceeding max_requests

print("\n#14")

class ApiClient:
    max_requests = 100

    def __init__(self, request):
        self.requests_made = request

    @property
    def requests_made(self):
        return self._requests_made

    @requests_made.setter
    def requests_made(self, request):
        if 0 <= request <= ApiClient.max_requests:
            self._requests_made = request
        else:
            raise ValueError


# ------------------
# Dependent Property Update
# ------------------

# 15. Create a class called Rectangle.
#
# Instance attributes:
# - _width
# - _height
#
# Add:
# - property width (with validation)
# - property height (with validation)
# - property perimeter = 2 * (width + height)

print("\n#15")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)



# ------------------
# Data Integrity (Multiple Constraints)
# ------------------

# 16. Create a class called Account.
#
# Instance attributes:
# - _username
# - _balance
#
# Add:
# - username property (non-empty string)
# - balance property (>= 0)

print("\n#16")

class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    @property
    def username(self):
        return self._username

    @property
    def balance(self):
        return self._balance

    @username.setter
    def username(self, username):
        if len(username) > 0:
            self._username = username
        else:
            raise ValueError

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError


# ------------------
# Property with Conditional Logic
# ------------------

# 17. Create a class called Student.
#
# Instance attribute:
# - _grade
#
# Add:
# - property grade
# - setter that only allows values between 0 and 100

print("\n#17")

class Student:
    def __init__(self, grade):
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade
        else:
            raise ValueError


# ------------------
# Concept Review
# ------------------

# 18. In comments, explain:
#
# - Why use _protected attributes instead of public ones?
# - What problem does @property solve?
# - When should you NOT use a setter?
# - What is a read-only property?
# - How do properties improve API design?

print("\n#18")

# To signal internal use and prevent direct external modification. Enforces encapsulation and allows controlled access via properties
# Allows controlled access to attributes
# When the attribute should be read-only or computed
# Only has a getter, no setters
# Separate internal implementation from external interfaces
