# ------------------
# Classes and Objects
# ------------------

# 1. Create a class called Dog.
# Instantiate two different objects from this class.
# Print their types.

print("\n#1")

class Dog():
    pass

dog1 = Dog()
dog2 = Dog()

print(type(dog1))
print(type(dog2))


# ------------------
# Attributes with __init__
# ------------------

# 2. Create a class called Student.
# It should have:
# - name
# - age
# Use __init__ to assign these attributes.
# Create an object and print its attributes.

print("\n#2")

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Joao", 26)

print(student1.name)
print(student1.age)


# ------------------
# Methods
# ------------------

# 3. Add a method to the Student class called introduce().
# The method should return a string using the object's attributes.
# Create an object and call the method.

print("\n#3")

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and my age is {self.age}"

student2 = Student("Jonh", 30)
print(student2.introduce())


# ------------------
# Understanding self
# ------------------

# 4. Create a class called Book.
# Add a method that returns the book's title.
# Explain (in comments) why self is required in the method.

print("\n#4")

class Book():
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

# self is required because it is returning a variable declared inside the class constructor


# ------------------
# Modifying Object State
# ------------------

# 5. Create a class called Counter.
# It should:
# - Start with a value of 0
# - Have a method called increment() that increases the value by 1
# - Have a method called decrement() that decreases the value by 1
# Create an object and modify its state.

print("\n#5")

class Counter():
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

counter = Counter()
print(counter.value)

counter.increment()
print(counter.value)

counter.decrement()
print(counter.value)


# ------------------
# Multiple Instances
# ------------------

# 6. Create a class called Car.
# Create two different objects.
# Change an attribute in one object.
# Observe that the other object is unaffected.

print("\n#6")

class Car():
    def __init__(self, brand):
        self.brand = brand

    def change_brand(self, new_brand):
        self.brand = new_brand

vw = Car("VW")
bmw = Car("BMW")

print(vw.brand)
print(bmw.brand)

bmw.change_brand("MERCEDES")
print(bmw.brand)


# ------------------
# Encapsulation (Protected Attribute)
# ------------------

# 7. Create a class called Example.
# Add an attribute with a single underscore (_variable).
# Access it from outside the class.
# Write a comment explaining what the underscore represents.

print("\n#7")

class Example():
    def __init__(self):
        self._example_var = 0

example = Example()

print(example._example_var)

# Convention that signals internal use inside the class only


# ------------------
# Encapsulation (Private Attribute)
# ------------------

# 8. Create a class called Secret.
# Add an attribute with double underscore (__variable).
# Create a method that returns this private attribute.
# Try to access it directly from outside the class.
# Observe what happens.

print("\n#8")

class Secret():
    def __init__(self):
        self.__secret_var = 0

    def get_secret_var(self):
        return self.__secret_var

secret = Secret()
# print(secret.__secret_var)
# raises error because variable is private, thus can't be accessed from outside the class

print(secret.get_secret_var())


# ------------------
# Real-World Modeling
# ------------------

# 9. Create a class called BankAccount.
# It should:
# - Have a balance attribute
# - Have a deposit() method
# - Have a withdraw() method
# - Have a method to display the balance
# Create an object and modify its state.

print("\n#9")

class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

account = BankAccount(100)
print(account.get_balance())

account.deposit(100)
print(account.get_balance())

account.withdraw(50)
print(account.get_balance())


# ------------------
# Concept Review
# ------------------

# 10. In comments, explain:
# - What is a class?
# - What is an object?
# - What is state?
# - What is encapsulation?
# - Why do we use __init__?

print("\n#10")

# A class is a blueprint of what an object is and what it should do
# An object is an instance of the class that contains its attributes and methods
# A state are the values of the objects
# Encapsulation means that a method or attribute can be private and not accessible outside the class
# __init__ is a constructor like method automatically executed when an object is instantiated
