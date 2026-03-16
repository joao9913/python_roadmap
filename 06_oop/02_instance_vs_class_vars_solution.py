# ------------------
# Instance Variables
# ------------------

# 1. Create a class called User.
# The class should store a username as an instance variable.
#
# Create two users with different usernames and print them.

print("\n#1")

class User:
    def __init__(self, name):
        self.name = name

user1 = User("Carlos")
user2 = User("Jonh")

print(user1.name)
print(user2.name)

# ------------------
# Class Variables
# ------------------

# 2. Create a class called Dog.
# Add a class variable called species with the value "Canis Familiaris".
#
# Create two dogs and print their species.

print("\n#2")

class Dog:
    species = "Canis Familiaris"

dog1 = Dog()
dog2 = Dog()

print(dog1.species)
print(dog2.species)


# ------------------
# Accessing Class Variables
# ------------------

# 3. Using the Dog class from the previous exercise:
# Print the class variable in two ways:
# - using the class itself
# - using an instance of the class

print("\n#3")

print(Dog.species)
print(dog1.species)


# ------------------
# Instance Independence
# ------------------

# 4. Create a class called Counter.
# It should have an instance variable called value starting at 0.
#
# Create two counters.
# Change the value of one counter and print both values
# to demonstrate they are independent.

print("\n#4")

class Counter:
    def __init__(self):
        self.value = 0

counter1 = Counter()
counter2 = Counter()

counter1.value = 10

print(counter1.value)
print(counter2.value)


# ------------------
# Shared Class Data
# ------------------

# 5. Create a class called GameSettings.
# Add a class variable called difficulty with value "Normal".
#
# Create two objects and print the difficulty from both.

print("\n#5")

class GameSettings:
    difficulty = "Normal"

game1 = GameSettings()
game2 = GameSettings()

print(game1.difficulty)
print(game2.difficulty)


# ------------------
# Modifying Class Variables
# ------------------

# 6. Using the GameSettings class:
# Change the difficulty to "Hard" using the class itself.
#
# Print the difficulty from both objects.

print("\n#6")

GameSettings.difficulty = "Hard"

print(game1.difficulty)
print(game2.difficulty)


# ------------------
# Shadowing Behavior
# ------------------

# 7. Create a class called Example.
# Add a class variable called value with value 10.
#
# Create two objects.
# Modify the value through only one object.
#
# Print:
# - value from object1
# - value from object2
# - value from the class
#
# Observe the behavior.

print("\n#7")

class Example:
    value = 10

example1 = Example()
example2 = Example()

example1.value = 20

print(example1.value)
print(example2.value)
print(Example.value)


# ------------------
# Realistic Modeling
# ------------------

# 8. Create a class called Student.
#
# Instance variables:
# - name
#
# Class variable:
# - school_name
#
# Create multiple students and print their names and school.

print("\n#8")

class Student:
    school_name = "School"

    def __init__(self, name):
        self.name = name

student1 = Student("Name1")
student2 = Student("Name2")

print(student1.name, student1.school_name)
print(student2.name, student2.school_name)


# ------------------
# Changing Shared Data
# ------------------
# ------------------
# Instance Variables
# ------------------

# 1. Create a class called User.
# The class should store a username as an instance variable.
#
# Create two users with different usernames and print them.

print("\n#1")

class User:
    def __init__(self, name):
        self.name = name

user1 = User("Carlos")
user2 = User("Jonh")

print(user1.name)
print(user2.name)

# ------------------
# Class Variables
# ------------------

# 2. Create a class called Dog.
# Add a class variable called species with the value "Canis Familiaris".
#
# Create two dogs and print their species.

print("\n#2")

class Dog:
    species = "Canis Familiaris"

dog1 = Dog()
dog2 = Dog()

print(dog1.species)
print(dog2.species)


# ------------------
# Accessing Class Variables
# ------------------

# 3. Using the Dog class from the previous exercise:
# Print the class variable in two ways:
# - using the class itself
# - using an instance of the class

print("\n#3")

print(Dog.species)
print(dog1.species)


# ------------------
# Instance Independence
# ------------------

# 4. Create a class called Counter.
# It should have an instance variable called value starting at 0.
#
# Create two counters.
# Change the value of one counter and print both values
# to demonstrate they are independent.

print("\n#4")

class Counter:
    def __init__(self):
        self.value = 0

counter1 = Counter()
counter2 = Counter()

counter1.value = 10

print(counter1.value)
print(counter2.value)


# ------------------
# Shared Class Data
# ------------------

# 5. Create a class called GameSettings.
# Add a class variable called difficulty with value "Normal".
#
# Create two objects and print the difficulty from both.

print("\n#5")

class GameSettings:
    difficulty = "Normal"

game1 = GameSettings()
game2 = GameSettings()

print(game1.difficulty)
print(game2.difficulty)


# ------------------
# Modifying Class Variables
# ------------------

# 6. Using the GameSettings class:
# Change the difficulty to "Hard" using the class itself.
#
# Print the difficulty from both objects.

print("\n#6")

GameSettings.difficulty = "Hard"

print(game1.difficulty)
print(game2.difficulty)


# ------------------
# Shadowing Behavior
# ------------------

# 7. Create a class called Example.
# Add a class variable called value with value 10.
#
# Create two objects.
# Modify the value through only one object.
#
# Print:
# - value from object1
# - value from object2
# - value from the class
#
# Observe the behavior.

print("\n#7")

class Example:
    value = 10

example1 = Example()
example2 = Example()

example1.value = 20

print(example1.value)
print(example2.value)
print(Example.value)


# ------------------
# Realistic Modeling
# ------------------

# 8. Create a class called Student.
#
# Instance variables:
# - name
#
# Class variable:
# - school_name
#
# Create multiple students and print their names and school.

print("\n#8")

class Student:
    school_name = "School"

    def __init__(self, name):
        self.name = name

student1 = Student("Name1")
student2 = Student("Name2")

print(student1.name, student1.school_name)
print(student2.name, student2.school_name)


# ------------------
# Changing Shared Data
# ------------------

# 9. Using the Student class:
# Change the school_name through the class.
#
# Print the school name for all existing students.

print("\n#9")

Student.school_name = "School 2"

print(student1.school_name)
print(student1.school_name)


# ------------------
# Concept Review
# ------------------

# 10. In comments, explain:
#
# - What is an instance variable?
# - What is a class variable?
# - When should you use a class variable?
# - What happens when an instance modifies a class variable?

print("\n#10")

# It's a variable that is only set to the given instance
# It's a variable that remains the same across instances of the class
# When you need the variable to be the same across instances (counters, global vars, etc)
# The class is only changed in that specific instance, not other instances nor the class itself

# 9. Using the Student class:
# Change the school_name through the class.
#
# Print the school name for all existing students.

print("\n#9")

Student.school_name = "School 2"

print(student1.school_name)
print(student2.school_name)


# ------------------
# Concept Review
# ------------------

# 10. In comments, explain:
#
# - What is an instance variable?
# - What is a class variable?
# - When should you use a class variable?
# - What happens when an instance modifies a class variable?

print("\n#10")

# It's a variable that is only set to the given instance
# It's a variable that remains the same across instances of the class
# When you need the variable to be the same across instances (counters, global vars, etc)
# The class is only changed in that specific instance, not other instances nor the class itself
