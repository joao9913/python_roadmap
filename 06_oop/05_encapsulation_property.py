"""
05_encapsulation_property.py
Topic: Encapsulation and @property
Goal: Learn how to control access to object data, protect state, and use Python properties for clean, safe interfaces
"""

# ------------------
# What is Encapsulation?
# ------------------

# Encapsulation is the idea of:
# - hiding internal data
# - controlling how its accessed and modified

# Instead of exposing attributes directly, we define rules for reading and writing them


# ------------------
# Public vs Protected vs Private (Convention)
# ------------------

# In Python, access modifiers are based on naming conventions

# public    -> name
# protected -> _name
# private   -> __name

class Example:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

obj = Example()

print("\n# Naming Conventions")
print(obj.public)       # Ok
print(obj._protected)   # Ok (but should be treated as internal)

# print(obj.__private)  # AttributeError

# Accessing private (name mangling)
print(obj._Example__private)


# ------------------
# Why Encapsulation Matters
# ------------------

# Problem: Direct access allows invalid state

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(100)
account.balance = -1000 # No control

print("\n# No encapsulation problem")
print(account.balance)


# ------------------
# Using Protected Attribute
# ------------------

# Convention: use _balance to signal unternal use

class SafeBankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

account = SafeBankAccount(100)
account.withdraw(50)

print("\n# Protected attribute")
print(account._balance) # Still acessible, but discourages


# ------------------
# Getter and Setter Methods (Old Style)
# ------------------

class BankAccountV2:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value >= 0:
            self._balance = value

account = BankAccountV2(100)

print("\n# Getter / Setter")
print(account.get_balance())

account.set_balance(200)
print(account.get_balance())


# ------------------
# @property (Pythonic way)
# ------------------

# Instead of get_balance() / set_balance()
# Python uses properties to make access look like attributes

class BankAccountV3:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

account = BankAccountV3(100)

print("\n# @property (getter)")
print(account.balance)  # looks like attribute, but is controlled


# ------------------
# @property Setter
# ------------------

class BankAccountV4:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

account = BankAccountV4(100)

print("\n# @property setter")
account.balance = 200
print(account.balance)

# account.balance = -100 # ignored (validation prevents it)


# ------------------
# Full Encapsulation with Validation
# ------------------

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:    # absolute zero
            self._celsius = value

temp = Temperature(25)

print("\n# Encapsulation with validation")
print(temp.celsius)

temp.celsius = -300 # invalid -> ignored
print(temp.celsius)


# ------------------
# Read-Only Property
# ------------------

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(2)

print("\n# Read-only property")
print(circle.area)

# circle.area = 10  # AttributeError (no setter)


# ------------------
# Property Depends On Other Attributes
# ------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self._width * self.height

rect = Rectangle(5, 10)

print("\n# Computed property")
print(rect.area)


# ------------------
# Key Takeaways
# ------------------

# - Encapsulation protects object state
# - Use _protected attributes for internal data
# - Avoid direct access when validation is needed
# - @property allows:
# - controlled access
# - clean syntax (obj.value instead of obj.get_value())
# - Use @property.setter to validate writes
# - You can create read-only attributes easily
