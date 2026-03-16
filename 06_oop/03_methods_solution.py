# ------------------
# Basic Method
# ------------------

# 1. Create a class called Greeter.
#
# Add a method called say_hello() that returns the string:
# "Hello!"
#
# Create an object and call the method.

print("\n#1")

class Greeter():
    def say_hello(self):
        return "Hello!"

greet = Greeter()
print(greet.say_hello())


# ------------------
# Using self
# ------------------

# 2. Create a class called Person.
#
# It should store:
# - name
#
# Add a method introduce() that returns:
# "My name is <name>"
#
# Create an object and call the method.

print("\n#2")

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

person = Person("Joao")
print(person.introduce())

# ------------------
# Reading Object State
# ------------------

# 3. Create a class called Temperature.
#
# It should store:
# - value (in Celsius)
#
# Add a method get_temperature() that returns the stored value.

print("\n#3")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def get_temperature(self):
        return self.celsius

temp = Temperature(2)
print(temp.get_temperature())


# ------------------
# Modifying Object State
# ------------------

# 4. Create a class called Counter.
#
# It should:
# - start with value = 0
#
# Add a method increment() that increases the value by 1.
#
# Create an object and call the method multiple times.
# Print the value after each call.

print("\n#4")

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()
counter.increment()
print(counter.value)

# ------------------
# Multiple Methods
# ------------------

# 5. Create a class called BankAccount.
#
# It should store:
# - balance
#
# Add methods:
# - deposit(amount)
# - withdraw(amount)
#
# Modify the balance and print the result.

print("\n#5")

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
# Method Returning a Calculation
# ------------------

# 6. Create a class called Rectangle.
#
# It should store:
# - width
# - height
#
# Add a method area() that returns the area.

print("\n#6")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


rectangle = Rectangle(20, 30)

print(rectangle.area())


# ------------------
# Method Calling Another Method
# ------------------

# 7. Create a class called ScoreTracker.
#
# It should store:
# - score (starting at 0)
#
# Add methods:
# - add_points(points)
# - reset()
# - get_score()
#
# Use these methods to modify and retrieve the score.

print("\n#7")

class ScoreTracker:
    def __init__(self):
        self.score = 0

    def add_points(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def get_score(self):
        return self.score

score = ScoreTracker()
score.add_points(10)
print(score.get_score())
score.reset()
print(score.get_score())


# ------------------
# Behavior Using Object Data
# ------------------

# 8. Create a class called Car.
#
# It should store:
# - brand
# - speed
#
# Add methods:
# - accelerate(amount) -> increases speed
# - brake(amount) -> decreases speed
#
# Print the speed after each operation.

print("\n#9")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

car = Car("BMW")
print(car.speed)

car.accelerate(100)
print(car.speed)
car.brake(100)
print(car.speed)


# ------------------
# Returning Information
# ------------------

# 9. Create a class called Student.
#
# It should store:
# - name
# - grade
#
# Add a method summary() that returns a sentence describing the student.

print("\n#9")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def summary(self):
        return f"{self.name} has {self.grade} grades"

student1 = Student("Name1", 2)
print(student1.summary())


# ------------------
# Concept Review
# ------------------

# 10. In comments, explain:
#
# - What is an instance method?
# - Why do methods receive "self"?
# - What is object state?
# - How can methods modify object state?
# - Why do methods often return values?

print("\n#10")

# An instance method is a method that are declared inside a class and alter behavior of each instance
# Because they change state of each instance
# Values of their attributes
# Define or change their attributes
# To print or return attributes from an instance of a class
