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

#print("\n#1")


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

#print("\n#2")


# ------------------
# Length Support
# ------------------

# 3. Create a class called Playlist.
#
# Instance attribute:
# - songs (list)
#
# Implement __len__ so len(playlist) returns number of songs

#print("\n#3")


# ------------------
# Equality Comparison
# ------------------

# 4. Create a class called Product.
#
# Instance attribute:
# - price
#
# Implement __eq__ so two products are equal if their prices are equal

#print("\n#4")


# ------------------
# Greater Than Comparison
# ------------------

# 5. Create a class called Score.
#
# Instance attribute:
# - value
#
# Implement __gt__ so one score is greater than another

#print("\n#5")


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

#print("\n#6")


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

#print("\n#7")


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

#print("\n#8")


# ------------------
# Setting Values
# ------------------

# 9. Extend Inventory.
#
# Implement __setitem__ so:
# inventory["item"] = value updates the dictionary

#print("\n#9")


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

#print("\n#10")


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

#print("\n#11")


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

#print("\n#12")


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

#print("\n#13")


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

#print("\n#14")


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

#print("\n#15")


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

#print("\n#16")


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

#print("\n#17")


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

#print("\n#18")
