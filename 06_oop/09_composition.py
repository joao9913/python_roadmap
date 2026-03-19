"""
09_composition.py
Topic: Composition
Goal: Understand how to use composition to build complex objects from smaller objects and reuse code
"""

# ------------------
# What Is Composition
# ------------------

# Composition is a way to build complex classes by including objects of other classes as attributes
# This allows us to reeuse functionality without inheritance
# Sometimes described as a "has-a" relationship:
# - A Car has an Engine
# - A Library has Books

print("\n# What Is Composition")

# ------------------
# Basic Example
# ------------------

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine    # Car "has an" Engine

    def start(self):
        return self.engine.start()  # Delegates work to Engine

engine = Engine()
car = Car(engine)

print(car.start())  # Engine started

print("\n-------------------------------------------------\n")


# ------------------
# Composition vs Inheritance
# ------------------

# Inheritance: "is-a" relationship
# Composition: "has-a" relationship

# Example:
# - Dog is an Animal (inheritance)
# - Car has an Engine (composition)

# Composition allows more flexibility
# - You can swap components at runtime

print("\n-------------------------------------------------\n")


# ------------------
# Using Composition to Build Complex Objects
# ------------------

class CPU:
    def compute(self):
        return "CPU computing"

class RAM:
    def load(self):
        return "RAM loading"

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def run(self):
        return f"{self.cpu.compute()} and {self.ram.load()}"

cpu = CPU()
ram = RAM()
pc = Computer(cpu, ram)
print(pc.run())     # CPU computing and RAM loading

print("\n-------------------------------------------------\n")


# ------------------
# Nested Composition
# ------------------

class Wheel:
    def rotate(self):
        return "Wheel rotating"

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, wheels, engine):
        self.wheels = wheels  # list of wheels
        self.engine = engine

    def drive(self):
        wheel_status = ", ".join([wheel.rotate() for wheel in self.wheels])
        return f"{self.engine.start()} | {wheel_status}"

engine = Engine()
wheels = [Wheel() for _ in range(4)]
car = Car(wheels, engine)
print(car.drive())

print("\n-------------------------------------------------\n")


# ------------------
# Advantages of Composition
# ------------------

# - Promotes code reuse
# - Avoids complex inheritance hierarchies
# - Encourages modular design
# - Components can be swapped easily

# Composition is widely used in frameworks and real-world applications:
# - A Window has Buttons, Labels, and Menus
# - A Library has Books, Shelves and Sections

print("\n-------------------------------------------------\n")

# ------------------
# Summary
# ------------------

# Composition allows you to:
# - Build objects from other objects
# - Create flexible and modular designs
# - Use delegation instead of inheritance
# - Implement "has-a" relationship
