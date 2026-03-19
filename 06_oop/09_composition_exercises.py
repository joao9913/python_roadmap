# 09_composition_exercises.py
# Topic: Composition Exercises
# Goal: Practice building classes using composition ("has-a" relationships)

# -------------------------------------------------
# 1. Basic Composition
# -------------------------------------------------

# Create:
# - Class Engine with method start() returning "Engine started"
# - Class Car that has an Engine as an attribute
# - Car should have method start() that delegates to Engine

# Test by creating a Car and calling start()

print("\n#1")

# -------------------------------------------------
# 2. Multiple Components
# -------------------------------------------------

# Create:
# - Class CPU with method compute()
# - Class RAM with method load()
# - Class Computer that has CPU and RAM
# - Computer.run() should call CPU.compute() and RAM.load()

# Test with an instance of Computer

print("\n#2")

# -------------------------------------------------
# 3. Nested Composition
# -------------------------------------------------

# Create:
# - Class Wheel with method rotate()
# - Class Engine with method start()
# - Class Car that has Engine and a list of 4 Wheels
# - Car.drive() should start the engine and rotate all wheels

print("\n#3")

# -------------------------------------------------
# 4. Swappable Components
# -------------------------------------------------

# Create:
# - Class Light with method turn_on()
# - Class Room that has a Light
# - Room.switch_light() calls Light.turn_on()
# - Swap the Light object with another Light instance and call switch_light() again

print("\n#4")

# -------------------------------------------------
# 5. Composition vs Inheritance
# -------------------------------------------------

# Create:
# - Class Animal with method eat()
# - Class Bird inherits from Animal
# - Class Zoo has a list of Animals
# - Zoo.feed_animals() should call eat() on all animals

print("\n#5")

# -------------------------------------------------
# 6. Delegation
# -------------------------------------------------

# Create:
# - Class Printer with method print_doc(doc)
# - Class Office that has a Printer
# - Office.print_document(doc) should delegate to Printer.print_doc()

print("\n#6")

# -------------------------------------------------
# 7. Real-World Example
# -------------------------------------------------

# Create a system:
# - Class Book with title
# - Class Library that has a list of Books
# - Library.list_titles() returns all book titles

print("\n#7")

# -------------------------------------------------
# 8. Nested Delegation
# -------------------------------------------------

# Create:
# - Class CPU with method compute()
# - Class GPU with method render()
# - Class Computer with CPU and GPU
# - Computer.run() calls CPU.compute() and GPU.render()

print("\n#8")

# -------------------------------------------------
# 9. Composition With Methods Returning Other Objects
# -------------------------------------------------

# Create:
# - Class Engine with start()
# - Class Car that has an Engine
# - Car.get_engine() should return the Engine object
# - Call engine.start() from the returned object

print("\n#9")

# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a system for a House:
# - Class Room
# - Class Light
# - Class House has multiple Rooms, each with Lights
# - House.turn_on_lights() should turn on all lights in all rooms

print("\n#10")
