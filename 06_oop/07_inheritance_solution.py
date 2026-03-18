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

print("\n#1")

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

employee = Employee("Jonh", 20000)
print(employee.name)
print(employee.salary)


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

print("\n#2")

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(3)
print(square.area())


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

print("\n#3")

class Animal():
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

bird = Bird("Bird", True)
print(bird.name)
print(bird.can_fly)



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

print("\n#4")

class Message:
    def __init__(self, content):
        self.content = content

    def display(self):
        return self.content

class EncryptedMessage(Message):
    def display(self):
        base_message = super().display()
        return base_message.upper()

message = EncryptedMessage("textexample")
print(message.display())


# -------------------------------------------------
# 5. isinstance() and issubclass()
# -------------------------------------------------

# Create:
# - Base class Vehicle
# - Child class Bike

# Write code that:
# - Checks if an object is instance of Vehicle
# - Checks if Bike is a subclass of Vehicle

print("\n#5")

class Vehicle:
    pass

class Bike(Vehicle):
    pass


bike = Bike()
print(isinstance(bike, Bike))
print(isinstance(bike, Vehicle))
print(issubclass(Bike, Vehicle))


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

print("\n#6")

class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, permissions):
        super().__init__(username)
        self.permissions = permissions

admin = Admin("Admin", "All")
print(admin.username)
print(admin.permissions)


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

print("\n#7")

class A:
    def example(self):
        print("Calling from class A")

class B(A):
    pass

class C(B):
    pass

c = C()
print(c.example())


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

print("\n#8")

class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
print(z.show())
print(Z.mro())


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

print("\n#9")

class Dog():
    def speak(self):
        return "Woof"

class Cat():
    def speak(self):
        return "Meow"

cat = Cat()
dog = Dog()

list_animals = [cat, dog]

for animal in list_animals:
    print(animal.speak())


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

print("\n#10")

class Account():
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance, transaction_fee):
        super().__init__(balance)
        self.transaction_fee = transaction_fee

    def add_transaction(self):
        self.balance -= self.transaction_fee

savings = SavingsAccount(10000, 100)
checkings = CheckingAccount(10000, 50)

savings.add_interest()
checkings.add_transaction()

print(savings.balance)
print(checkings.balance)
