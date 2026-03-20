from abc import ABC, abstractmethod

# -------------------------------------------------
# 1. Basic Abstract Class
# -------------------------------------------------

# Create an abstract class Shape with an abstract method area()
# Then create a subclass Circle that implements area()

print("\n#1")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2

circle = Circle(2)
print(circle.area())


# -------------------------------------------------
# 2. Multiple Abstract Methods
# -------------------------------------------------

# Create an abstract class Vehicle with:
# - abstract method start_engine()
# - abstract method stop_engine()
# Then create a subclass Car implementing both methods

print("\n#2")

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Starting car engine"

    def stop_engine(self):
        return "Stopping car engine"

car = Car()
print(car.start_engine())
print(car.stop_engine())


# -------------------------------------------------
# 3. Abstract Method with Default Behavior
# -------------------------------------------------

# Create an abstract class Animal with abstract method speak()
# Give speak() a default print("Some generic sound")
# Create subclass Dog that calls super().speak() and then prints "Woof!"

print("\n#3")

class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

dog = Dog()
dog.speak()


# -------------------------------------------------
# 4. Prevent Instantiation
# -------------------------------------------------

# Try to create an instance of an abstract class directly
# Observe the error

print("\n#4")

class Example(ABC):
    @abstractmethod
    def abstract_method(self):
        print()

#example = Example()
#print(example)


# -------------------------------------------------
# 5. Polymorphism with Abstract Classes
# -------------------------------------------------

# Create an abstract class Payment with abstract method pay()
# Create subclasses CreditCardPayment and PayPalPayment
# Store them in a list and call pay() on each

print("\n#5")

class Payment(ABC):
    @abstractmethod
    def pay(self):
        return ""

class CreditCardPayment(Payment):
    def pay(self):
        return "Paying with credit card"

class PayPalPayment(Payment):
    def pay(self):
        return "Paying with paypal"

payment_list = [CreditCardPayment(), PayPalPayment()]

for payment in payment_list:
    print(payment.pay())


# -------------------------------------------------
# 6. Abstract Class with Constructor
# -------------------------------------------------

# Create an abstract class Employee with:
# - __init__(name)
# - abstract method calculate_pay()
# Subclass Manager that implements calculate_pay()

print("\n#6")

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass


class Manager(Employee):
    def calculate_pay(self):
        return 1000 + 340

manager = Manager("Manager1")
print(manager.calculate_pay())


# -------------------------------------------------
# 7. Nested Abstract Classes
# -------------------------------------------------

# Create abstract class Logger with abstract method log()
# Create abstract class FileLogger(Logger)
# Create subclass TextLogger implementing log()

print("\n#7")

class Logger(ABC):
    @abstractmethod
    def log(self):
        pass

class FileLogger(Logger):
    pass

class TextLogger(FileLogger):
    def log(self):
        return "Text logger | log"

text_logger = TextLogger()
print(text_logger.log())


# -------------------------------------------------
# 8. Enforcing Interfaces
# -------------------------------------------------

# Create abstract class Database with abstract method connect()
# Create subclass MySQLDatabase implementing connect()
# Demonstrate that another subclass without connect() cannot be instantiated

print("\n#8")

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting SQL Database"

class AnotherDatabase(Database):
    pass

sql_database = MySQLDatabase()
print(sql_database.connect())

# another_database = AnotherDatabase()


# -------------------------------------------------
# 9. Abstract Properties
# -------------------------------------------------

# Create abstract class Product with abstract property price
# Subclass Book implementing price as a property

print("\n#9")

class Product(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

class Book(Product):
    @property
    def price(self):
        return 19

book = Book()
print(book.price)


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create abstract class Strategy with abstract method execute()
# Implement 3 different trading strategies as subclasses
# Store them in a list and call execute() on each

print("\n#10")

class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class Strategy1(Strategy):
    def execute(self):
        return "Executing strategy 1"

class Strategy2(Strategy):
    def execute(self):
        return "Executing strategy 2"

class Strategy3(Strategy):
    def execute(self):
        return "Executing strategy 3"

strategy_list = [Strategy1(), Strategy2(), Strategy3()]

for strategy in strategy_list:
    print(strategy.execute())
