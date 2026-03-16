# ------------------
# Creating Classes
# ------------------

# 1. Create a class called Animal.
# Create two objects from this class.
# Print their types.

print("\n#1")

class Animal:
    pass

animal1 = Animal()
animal2 = Animal()

print(type(animal1))
print(type(animal2))


# ------------------
# Attributes with __init__
# ------------------

# 2. Create a class called User.
# It should store:
# - username
# - email
#
# Create one object and print both attributes.

print("\n#2")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User("admin", "admin@email.com")

print(user1.email)
print(user1.username)


# ------------------
# Multiple Objects
# ------------------

# 3. Create a class called Product.
# It should store:
# - name
# - price
#
# Create two different products and print their attributes.

print("\n#3")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("product1", 20)
product2 = Product("product2", 30)

print(product1.name, product1.price)
print(product2.name, product2.price)


# ------------------
# Methods
# ------------------

# 4. Create a class called Rectangle.
# It should store:
# - width
# - height
#
# Add a method called area() that returns the rectangle area.
# Create an object and call the method.

print("\n#4")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


rectangle = Rectangle(20, 30)

print(rectangle.area())


# ------------------
# Methods Using Object Data
# ------------------

# 5. Create a class called Person.
# It should store:
# - name
# - age
#
# Add a method called describe() that returns a sentence describing the person.

print("\n#5")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age}"

person1 = Person("Jonh", 20)
print(person1.describe())


# ------------------
# Object State
# ------------------

# 6. Create a class called Counter.
# It should:
# - Start with value = 0
# - Have a method increment() that increases the value by 1
#
# Create an object and call increment() multiple times.
# Print the value after each call.

print("\n#6")

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()
print(counter.value)
counter.increment()
print(counter.value)
counter.increment()
print(counter.value)


# ------------------
# Modifying Object State
# ------------------

# 7. Create a class called BankAccount.
# It should store:
# - balance
#
# Add methods:
# - deposit(amount)
# - withdraw(amount)
#
# Modify the balance using these methods and print the result.

print("\n#7")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(100)
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(50)
print(account.balance)

# ------------------
# Instance Independence
# ------------------

# 8. Create a class called LightSwitch.
# It should store a state: "on" or "off".
#
# Add methods:
# - turn_on()
# - turn_off()
#
# Create two switches and demonstrate that changing one
# does not affect the other.

print("\n#8")

class LightSwitch:
    def __init__(self):
        self.state = True

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

switch1 = LightSwitch()
switch2 = LightSwitch()

switch1.turn_on()
switch2.turn_off()

print(switch1.state)
print(switch2.state)

# ------------------
# Method Returning Data
# ------------------

# 9. Create a class called Temperature.
# It should store a temperature value in Celsius.
#
# Add a method get_fahrenheit()
# that returns the converted temperature.

print("\n#9")

class Temperature:
    def __init__(self, temp):
        self.temperature = temp

    def get_fahrenheit(self):
        return self.temperature * 1.8 + 32

temp = Temperature(0)
print(temp.get_fahrenheit())


# ------------------
# Concept Review
# ------------------

# 10. In comments, explain:
#
# - What is a class?
# - What is an object (instance)?
# - What is the purpose of __init__?
# - What does "self" represent?
# - What does it mean that objects have state?

print("\n#10")

# Defines the structure (attributes) and behaviour (methods) that objects created from it will have
# An object is an instance of a class
# The purpose of init is to initialize the attributes of the class. Runs automatically upon instanciation
# Self represents the specific instance of the class that is calling the method
# Means that each object contains its own set of information.
