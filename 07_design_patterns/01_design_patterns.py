"""
12_design_patterns.py
Topic: Design Patterns
Goal: Understand common design patterns in Python, their purpose, and how to implement them effectively
"""

# ------------------
# What Are Design Patterns
# ------------------

# Design patterns are reusable solutions to common software design problems
# They provide best practices for structuring code and solving recurring issues.

# Categories:
# - Creational: deal with object creation (e.g., Singleton, Factory)
# - Structural: deal with object composition (e.g., Adapter, Decorator)
# - Behavioral: deal with object interaction and responsability (e.g., Strategy, Observer)


# ------------------
# Singleton Pattern
# ------------------

# A Singleton is a design pattern that ensures:
# - 1. A class has only one instance in the entire application
# - 2. That instance is globally accessible

# It's basically a single shared resource, for example:
# - A config manager (so all parts of your app read/write the same config)
# - A logging system (so logs are centralized)
# - A data base connection pool (to avoid creating multiple connections unnecessarily)


# Why is this pattern needed?
# - Centralized State   - You want one single source of truth
# - Resource Management - Some objects are expensive to create (like DB connections), so you only want one
# - Consistency         - All parts of the code should share the same instance for certain classes

class SingletonMeta(type):
    _instances = {} # Dictionary to hold existing instances

    def __call__(cls, *args, **kwargs):
        # This method is called when we "instantiate" the class (e.g. Singleton(10))

        if cls not in cls._instances:
            # If we haven't created an instance yet, create one

            cls._instances[cls] = super().__call__(*args, **kwargs)

        # Return the stored instance
        return cls._instances[cls]


# SingletoneMeta is a metaclass. A metaclass controls how classes behave.
# Normally, classes are instances of "type".
# By creating a costum metaclass, you can intercept class instantiation

# - __call__ in a metaclass is triggered every time the class is instantiated
# This allows us to control the creation of instances

# _instances stores one instance per class. If the class hasn't been instantiated yet, we create it.
# Otherwise, we return the already created instance.


class Singleton(metaclass = SingletonMeta):
    def __init__(self, value):
        self.value = value

# metaclass = SingletonMeta -> this tells Python: "Use SingletonMeta to handle creation of this class"

# When you call Singleton(10), Python calls the "__call__" method in th metaclass instead of directly
# creating a new object.

# _instances ensures only one object is ever created.


s1 = Singleton(10)
# - SingletonMeta.__call__ is triggered
# - _instances doesn't have Singleton yet -> a new instance is created and stores
# - __init__ sets value = 10

s2 = Singleton(20)
# - SingletonMeta.__call__ is triggered again
# - _instances already has the Singleton instance -> return the same instance
# - __init__ is not called again, so the value remains 10.


print(s1.value)     #10
print(s2.value)     #10, same instance


# When To Use Singleton
# - When you need exactly one instance per class
#   - Logger (centralized logging)
#   - Configuration manager (shared configuration
#   - Thread pool or DB connection manager
#   - Cache manager


# ------------------
# Factory Pattern
# ------------------

# A Factory is a design pattern that:
# - Creates objects without exposing the exact class being instantiated
# - Uses a method to decide which object to create

# It's basically a "centralized object creator", for example:
# - Creating different trading strategies based on name
# - Creating UI components (Button, Input, etc)
# - Creating different payment methods (CreditCard, Paypal, Crypto)


# Why is this pattern needed?
# - Decoupling          - Code does not depend on concrete classes
# - Flexibility         - Easy to add new types without changing existing code
# - Centralized Logic   - Object creation is handled in one place


class Shape:
    def draw(self):
        raise NotImplemented

class Circle(Shape):
    def draw(self):
        return "Circle drawn"

class Square(Shape):
    def draw(self):
        return "Square drawn"

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        # This method decides which object to create

        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()

        # If type is unknown, return None (or could raise an error)
        return None

# ShapeFactory.create_shape() is a centralized method that creates objects
# Instead of doing: Circle or Square() directly, we delegate creation to the factory

# This removes direct dependency on concrete classes

circle = ShapeFactory.create_shape("circle")
square = ShapeFactory.create_shape("square")

print(circle.draw())
print(square.draw())

# Step By Step:
# - We call ShapeFactory.create_shape("circle")
# - The factory checks the input
# - It returns a Circle object
# - We call draw() without caring about the actual class

# When To Use Factory
# - When object creation logic is complex
# - When you want to avoid direct class instantiation
# - When you expect to add more types later
# - When working with interfaces or base classes

# Instead of:
#   obj = Circle()

# You do:
#   obj = ShapeFactory.create_shape("circle")

# So your code depends on "Shape", not "Circle"


# ------------------
# Strategy Pattern
# ------------------

# A Strategy is a design pattern that:
# - Defines a family of algorithms
# - Encapsulates each one into separate classes
# - Makes them interchangeable at runtime

# It's basically "plug-and-play behavior", for example:
# - Different trading strategies (breakout, mean reversion, scalping)
# - Different sorting or calculation methods
# - Different risk management rules


# Why is this pattern needed?
# - Flexibility     - You can switch behavior at runtime
# - Separation      - Each algorithm is isolated in its own class
# - Clean Code      - Avoids large if/else blocks
# - Scalability     - Easy to add new strategies without modifying existing code


class Strategy:
    def execute(self, data):
        raise NotImplementedError


# Each class represents a different algorithm (strategy)

class StrategyAdd(Strategy):
    def execute(self, data):
        return sum(data)

class StrategyMultiply(Strategy):
    def execute(self, data):
        result = 1
        for d in data:
            result *= d
        return result


# Context is the class that USES the strategy
# It doesn't care HOW the strategy works, only that it has execute()

class Context:
    def __init__(self, strategy):
        self.strategy = strategy    # current strategy

    def set_strategy(self, strategy):
        # Allows switching strategy at runtime
        self.strategy = strategy

    def execute_strategy(self, data):
        # Delegates execution to the strategy
        return self.strategy.execute(data)


# How this works step-by-step:
# - We create a Context with StrategyAdd
# - Context stores the strategy
# - When execute_strategy() is called, it delegates to the strategy

context = Context(StrategyAdd())
print(context.execute_strategy([1, 2, 3]))

# We can switch strategy at runtime

context.set_strategy(StrategyMultiply())
print(context.execute_strategy([1, 2, 3]))

# Key Idea:
# Context does NOT know what the strategy does
# It only knows it can call execute()

# This allows us to swap behavior without changing Context


# When To Use Strategy
# - When you have multiple ways to perform a task
# - When you want to switch logic dynamically
# - When you want to avoid large conditional statements
# - When each behavior should be isolated and reusable

# Example mindset:
# Instead of:
#   if strategy == "breakout":
#       ...
#   elif strategy == "mean_reversion":
#       ...

# You do:
#   context.set_strategy(BreakoutStrategy())
#   context.execute_strategy(data)


# ------------------
# Observer Pattern
# ------------------

# An Observer is a design pattern that:
# - Defines a one-to-many relationship between objects
# - When one object (Subject) changes state, all dependent objects (Observers) are notified automatically

# It's basically an "event system", for example:
# - Trading signals notifying multiple systems (logger, UI, execution)
# - Price feed updating multiple indicators
# - UI events (button click updates multiple components)


# Why is this pattern needed?
# - Decoupling          - Subject does not need to know details of observers
# - Scalability         - Easily add/remove observers
# - Event-driven        - Automatically react to changes
# - Clean architecture  - Avoid tight coupling between components


class Subject:
    def __init__(self):
        self._observers = []    # list of subscribers

    def attach(self, observer):
        # Add a new observer
        self._observers.append(observer)

    def detach(self, observer):
        # Remove an observer
        self._observers.remove(observer)

    def notify(self, message):
        # Notify all observers
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError

# Each observer implements its own reaction to the event

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

# How this works step-by-step:

# - Create a Subject (the event source)
# - Create multiple Observers (listeners)
# - Attach observers to the subject
# - When something happens, subject notifies all observers

subject = Subject()
observer1 = ConcreteObserver("Observer1")
observer2 = ConcreteObserver("Observer2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Event happened!")
# Output:
# Observer1 received: Event happened!
# Observer2 received: Event happened!

# Key idea:
# Subject does NOT know what observers do
# It only knows they have an update() method

# This allows adding new observers without modifying Subject

# When To Use Observer
# - When multiple objects need to react to the same event
# - When building event-driven systems
# - When you want to decouple sender and receivers
# - When state changes should automatically trigger actions

# Example mindset:
# Instead of:
#   strategy executes trade
#   logger logs trade
#   UI updates trade
#   notifier sends alert

# You do:
#   subject.notify("Trade executed")

# And attach:
# - LoggerObserver
# - UIObserver
# - NotificationObserver


# ------------------
# Summary
# ------------------

# Key points:
# - Design patterns solve recurring problems in software design
# - Singleton ensures single instance
# - Factory abstracts object creation
# - Strategy encapsulates interchangeable algorithms
# - Observer manages dependencies and notifications
# - Patterns improve code maintainability, scalability and readability
