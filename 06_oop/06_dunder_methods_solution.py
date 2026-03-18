# 06_dunder_methods_exercises.py

# ------------------
# String Representation
# ------------------

# 1. Create a class called Book.
#
# Instance attributes:
# - title
# - author
#
# Add a __str__ method that returns:
# "Title by Author"

print("\n#1")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Book Name", "Jonh Doe")
print(book)


# ------------------
# Debug Representation
# ------------------

# 2. Create a class called User.
#
# Instance attribute:
# - username
#
# Add a __repr__ method that returns:
# User(username='name')

print("\n#2")

class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User(username={self.username!r})"

user = User("Admin")
print(user)

# ------------------
# Length Support
# ------------------

# 3. Create a class called Playlist.
#
# Instance attribute:
# - songs (list)
#
# Implement __len__ so len(playlist) returns number of songs

print("\n#3")

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

list_songs = ["song1", "song2", "song3"]
playlist = Playlist(list_songs)

print(len(playlist))


# ------------------
# Equality Comparison
# ------------------

# 4. Create a class called Product.
#
# Instance attribute:
# - price
#
# Implement __eq__ so two products are equal if their prices are equal

print("\n#4")

class Product:
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            raise NotImplemented

        return self.price == other.price

product1 = Product(12)
product2 = Product(12)

print(product1 == product2)


# ------------------
# Greater Than Comparison
# ------------------

# 5. Create a class called Score.
#
# Instance attribute:
# - value
#
# Implement __gt__ so one score is greater than another

print("\n#5")

class Score:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented

        return self.value > other.value

score1 = Score(30)
score2 = Score(20)

print(score1 > score2)

# ------------------
# Addition of Objects
# ------------------

# 6. Create a class called Vector.
#
# Instance attributes:
# - x
# - y
#
# Implement __add__ so:
# v1 + v2 returns a new Vector with summed values

print("\n#6")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)


# ------------------
# Boolean Behavior
# ------------------

# 7. Create a class called Wallet.
#
# Instance attribute:
# - balance
#
# Implement __bool__ so:
# - True if balance > 0
# - False otherwise

print("\n#7")

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0

wallet = Wallet(-100)

if wallet:
    print("More than 0")
else:
    print("Less than 0 ")


# ------------------
# Index Access
# ------------------

# 8. Create a class called Inventory.
#
# Instance attribute:
# - items (dictionary)
#
# Implement __getitem__ so:
# inventory["item_name"] returns the value

print("\n#8")

class Inventory:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

inv = Inventory({"a": 1, "b": 2})
print(inv["a"])


# ------------------
# Setting Values
# ------------------

# 9. Extend Inventory.
#
# Implement __setitem__ so:
# inventory["item"] = value updates the dictionary

print("\n#9")

class Inventory:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

inv = Inventory({"a": 1, "b": 2})
inv["c"] = 3
print(inv["c"])


# ------------------
# Callable Object
# ------------------

# 10. Create a class called Multiplier.
#
# Instance attribute:
# - factor
#
# Implement __call__ so:
# obj(value) returns value * factor

print("\n#10")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

mul = Multiplier(2)
print(mul(5))


# ------------------
# Combined Behavior
# ------------------

# 11. Create a class called Cart.
#
# Instance attribute:
# - items (list of prices)
#
# Implement:
# - __len__ → number of items
# - __str__ → "Cart with X items"
# - __add__ → combine two carts into a new one

print("\n#11")

class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Cart with {len(self)} items."

    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented

        return Cart(self.items + other.items)


list_items = ["item1", "item2", "item3"]
list_items2 = ["item4", "item5"]

cart = Cart(list_items)
cart2 = Cart(list_items2)

print(len(cart))
print(cart)

combined_cart = cart + cart2
print(combined_cart)


# ------------------
# Safe Comparison
# ------------------

# 12. Create a class called Temperature.
#
# Instance attribute:
# - value
#
# Implement __eq__ but:
# - Return NotImplemented if compared with non-Temperature object

print("\n#12")

class Temperature:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.value == other.value

        return NotImplemented

temp1 = Temperature(1)
temp2 = Temperature(2)
print(temp1 == temp2)


# ------------------
# Custom Container Behavior
# ------------------

# 13. Create a class called Stack.
#
# Instance attribute:
# - items (list)
#
# Implement:
# - __len__
# - __getitem__ (index access)
#
# Bonus: prevent invalid index access if possible

print("\n#13")

class Stack:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if(index < len(self.items)):
            return self.items[index]

        return ValueError


list_stack = [1, 2, 3]

stack = Stack(list_stack)
print(len(stack))
print(stack[0])


# ------------------
# Advanced Addition Logic
# ------------------

# 14. Create a class called Time.
#
# Instance attributes:
# - hours
# - minutes
#
# Implement __add__ so:
# - adding two Time objects returns a normalized time
#   (e.g. 90 minutes → 1 hour 30 minutes)

print("\n#14")

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        sum_hours = self.hours + other.hours
        sum_minutes = self.minutes + other.minutes

        if sum_minutes >= 60:
            sum_hours += sum_minutes // 60
            sum_minutes = sum_minutes % 60


        return Time(sum_hours, sum_minutes)

time1 = Time(2, 30)
time2 = Time(1, 50)
time3 = time1 + time2
print(time3.hours, ":", time3.minutes)


# ------------------
# Truthiness with Multiple Conditions
# ------------------

# 15. Create a class called UserSession.
#
# Instance attributes:
# - is_logged_in (bool)
# - token (string or None)
#
# Implement __bool__ so:
# - True only if logged in AND token exists

print("\n#15")

class UserSession:
    def __init__(self, is_logged_in, token):
        self.is_logged_in = is_logged_in
        self.token = token

    def __bool__(self):
        return self.is_logged_in and bool(self.token)

user_session = UserSession(False, "token1")

if user_session:
    print("Session logged in")
else:
    print("Session not logged in")


# ------------------
# Immutable-like Behavior
# ------------------

# 16. Create a class called Point.
#
# Instance attributes:
# - x
# - y
#
# Implement:
# - __add__ (returns new Point)
# - DO NOT modify original objects

print("\n#16")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
point3 = point1 + point2
print(point3.x, point3.y)


# ------------------
# Defensive Programming
# ------------------

# 17. Create a class called Price.
#
# Instance attribute:
# - amount
#
# Implement __add__ so:
# - Only allow adding another Price
# - Otherwise raise TypeError

print("\n#17")

class Price:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Price):
            return Price(other.amount + self.amount)

        raise TypeError

price1 = Price(1)
price2 = Price(2)
price3 = price1 + price2
print(price3.amount)


# ------------------
# Concept Review
# ------------------

# 18. In comments, explain:
#
# - Why does __repr__ exist if we already have __str__?
# - What is NotImplemented used for?
# - Why should __add__ return a new object instead of modifying self?
# - When would you override __bool__?
# - Why are dunder methods important for API design?

print("\n#18")

# It exists for debugging, its more detailed than str
# NotImplement is used when comparing different object types
# Because it is adding two different objects, thus it cant modify one of them
# When you want custom objects to evaluate in boolean contexts
# Dunder methods allow your objects to integrate with Python’s core syntax
