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

print("\n#1")

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())


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

print("\n#2")

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Bird:
    def speak(self):
        return "Chirp"


list_animals = [Dog(), Cat(), Bird()]

for animal in list_animals:
    print(animal.speak())


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

print("\n#3")

class Robot:
    def speak(self):
        return "Robot speaking"

class Human:
    def speak(self):
        return "Human speaking"

def make_sound(obj):
    print(obj.speak())

robot = Robot()
human = Human()

make_sound(robot)
make_sound(human)


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

print("\n#4")

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

list_animals = [Dog(), Cat(), Animal()]

for animal in list_animals:
    print(animal.speak())


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

print("\n#5")

def process(obj):
    obj.run()

class Class1:
    def run(self):
        print("Running class 1")

class Class2:
    def run(self):
        print("Running class 2")

class1 = Class1()
class2 = Class2()

process(class1)
process(class2)


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

print("\n#6")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

        raise NotImplemented

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y)


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

print("\n#7")

class Dog:
    def speak(self):
        return "Woof"

class Car:
    pass

list_speak = [Dog(), Car()]

#for item in list_speak:
    #print(item.speak())


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

print("\n#8")

def describe(obj):
    obj.describe()

class Class1:
    def describe(self):
        print("I am class 1")

class Class2:
    def describe(self):
        print("I am class 2")

c1 = Class1()
c2 = Class2()

describe(c1)
describe(c2)


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

print("\n#9")

class CreditCardPayment:
    def pay(self):
        return "Pay with credit card"

class PayPalPayment:
    def pay(self):
        return "Pay with paypal"

class CryptoPayment:
    def pay(self):
        return "Pay with crypto"

pay_list = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]

for payment in pay_list:
    print(payment.pay())


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

print("\n#10")

class Strategy1:
    def execute_trade(self):
        return "Running strategy 1"

class Strategy2:
    def execute_trade(self):
        return "Running strategy 2"

class Strategy3:
    def execute_trade(self):
        return "Running strategy 3"

list_strategies = [Strategy1(), Strategy2(), Strategy3()]

for strat in list_strategies:
    print(strat.execute_trade())
