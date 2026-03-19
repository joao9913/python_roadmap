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

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

engine = Engine()
car = Car(engine)
print(car.start())

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

class CPU:
    def compute(self):
        return "CPU Computing"

class RAM:
    def load(self):
        return "RAM Loading"

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def run(self):
        return f"Running: {self.cpu.compute()} and {self.ram.load()}"

cpu = CPU()
ram = RAM()
pc = Computer(cpu, ram)
print(pc.run())

# -------------------------------------------------
# 3. Nested Composition
# -------------------------------------------------

# Create:
# - Class Wheel with method rotate()
# - Class Engine with method start()
# - Class Car that has Engine and a list of 4 Wheels
# - Car.drive() should start the engine and rotate all wheels

print("\n#3")

class Wheel:
    def rotate(self):
        return "Wheels rotating"

class Engine:
    def start(self):
        return "Engine starting"

class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels    # list of wheels

    def drive(self):
        wheel_status = ", ".join([wheel.rotate() for wheel in self.wheels])
        return f"Engine: {self.engine.start()} | Wheels: {wheel_status}"

engine = Engine()
list_wheels = [Wheel() for _ in range(4)]
car = Car(engine, list_wheels)
print(car.drive())


# -------------------------------------------------
# 4. Swappable Components
# -------------------------------------------------

# Create:
# - Class Light with method turn_on()
# - Class Room that has a Light
# - Room.switch_light() calls Light.turn_on()
# - Swap the Light object with another Light instance and call switch_light() again

print("\n#4")

class Light:
    def turn_on(self):
        return "Light is on"

class Room:
    def __init__(self, light):
        self.light = light

    def switch_light(self):
        return self.light.turn_on()

light1 = Light()
room = Room(light1)
print(room.switch_light())

light2 = Light()
room.light = light2
print(room.switch_light())


# -------------------------------------------------
# 5. Composition vs Inheritance
# -------------------------------------------------

# Create:
# - Class Animal with method eat()
# - Class Bird inherits from Animal
# - Class Zoo has a list of Animals
# - Zoo.feed_animals() should call eat() on all animals

print("\n#5")

class Animal:
    def eat(self):
        return "Animal eating"

class Bird(Animal):
    pass

class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def feed_animals(self):
        for animal in self.animals:
            print(animal.eat())

list_animals = [Bird() for _ in range(3)]

zoo = Zoo(list_animals)
zoo.feed_animals()


# -------------------------------------------------
# 6. Delegation
# -------------------------------------------------

# Create:
# - Class Printer with method print_doc(doc)
# - Class Office that has a Printer
# - Office.print_document(doc) should delegate to Printer.print_doc()

print("\n#6")

class Printer:
    def print_doc(self, doc):
        return f"Printing {doc}"

class Office:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self, doc):
        return self.printer.print_doc(doc)

printer = Printer()
office = Office(printer)

print(office.print_document("Document 1"))


# -------------------------------------------------
# 7. Real-World Example
# -------------------------------------------------

# Create a system:
# - Class Book with title
# - Class Library that has a list of Books
# - Library.list_titles() returns all book titles

print("\n#7")

class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self, books):
        self.books = books

    def list_titles(self):
        for book in self.books:
            print(book.title)

book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")

list_books = [book1, book2, book3]

library = Library(list_books)
library.list_titles()


# -------------------------------------------------
# 8. Nested Delegation
# -------------------------------------------------

# Create:
# - Class CPU with method compute()
# - Class GPU with method render()
# - Class Computer with CPU and GPU
# - Computer.run() calls CPU.compute() and GPU.render()

print("\n#8")

class CPU:
    def compute(self):
        return "Computing CPU"

class GPU:
    def render(self):
        return "Rendering GPU"

class Computer:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def run(self):
        return f"CPU: {self.cpu.compute()} | GPU: {self.gpu.render()}"

cpu = CPU()
gpu = GPU()
pc = Computer(cpu, gpu)
print(pc.run())

# -------------------------------------------------
# 9. Composition With Methods Returning Other Objects
# -------------------------------------------------

# Create:
# - Class Engine with start()
# - Class Car that has an Engine
# - Car.get_engine() should return the Engine object
# - Call engine.start() from the returned object

print("\n#9")

class Engine:
    def start(self):
        return "Starting engine"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def get_engine(self):
        return self.engine

engine = Engine()
car = Car(engine)
print(car.get_engine().start())


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a system for a House:
# - Class Room
# - Class Light
# - Class House has multiple Rooms, each with Lights
# - House.turn_on_lights() should turn on all lights in all rooms

print("\n#10")

class Light:
    def turn_on(self):
        return "Light has turned on."


class Room:
    def __init__(self, lights):
        self.lights = lights


class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def turn_on_lights(self):
        for room in self.rooms:
            for light in room.lights:
                print(light.turn_on())


lights = [Light(), Light(), Light()]
rooms = [Room(lights), Room(lights)]
house = House(rooms)

house.turn_on_lights()
