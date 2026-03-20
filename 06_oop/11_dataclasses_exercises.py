"""
12_dataclasses_exercises.py
Topic: Dataclasses
Goal: Practice creating and using dataclasses, handling defaults, immutability,
      ordering, and post-init processing.
"""

# -------------------------------------------------
# 1. Basic Dataclass
# -------------------------------------------------

# Create a dataclass Book with:
# - title (str)
# - author (str)
# Create an instance and print it

print("\n#1")


# -------------------------------------------------
# 2. Default Values
# -------------------------------------------------

# Create a dataclass Book with:
# - title (str)
# - author (str)
# - pages (int, default=100)
# Create two books, one with default pages and one with custom pages, then print pages

print("\n#2")


# -------------------------------------------------
# 3. Immutability
# -------------------------------------------------

# Create a dataclass Point with:
# - x (int)
# - y (int)
# Make the dataclass frozen
# Try changing x after instantiation (observe the behavior)

print("\n#3")


# -------------------------------------------------
# 4. Ordering
# -------------------------------------------------

# Create a dataclass Player with:
# - score (int)
# - name (str)
# Enable ordering
# Create two players and compare them using < and >

print("\n#4")


# -------------------------------------------------
# 5. Custom Method
# -------------------------------------------------

# Create a dataclass Circle with:
# - radius (float)
# Add a method area() that calculates the area of the circle
# Create an instance and print the area

print("\n#5")


# -------------------------------------------------
# 6. Post-Init Processing
# -------------------------------------------------

# Create a dataclass Rectangle with:
# - width (int)
# - height (int)
# - area (int, default 0)
# Use __post_init__ to automatically calculate area after initialization
# Create an instance and print the area

print("\n#6")


# -------------------------------------------------
# 7. Field with default_factory
# -------------------------------------------------

# Create a dataclass Inventory with:
# - items (list, use default_factory=list)
# Create two instances and add an item to the first
# Print the second instance's items to confirm they are separate lists

print("\n#7")


# -------------------------------------------------
# 8. Dataclass Comparison
# -------------------------------------------------

# Create a dataclass Product with:
# - price (float)
# - name (str)
# Enable ordering
# Create two products and check which one is greater

print("\n#8")


# -------------------------------------------------
# 9. Nested Dataclasses
# -------------------------------------------------

# Create a dataclass Engine with:
# - horsepower (int)
# Create a dataclass Car with:
# - model (str)
# - engine (Engine)
# Instantiate a car with an engine and print engine horsepower

print("\n#9")


# -------------------------------------------------
# 10. Design Challenge
# -------------------------------------------------

# Create a dataclass Student with:
# - name (str)
# - grades (list of floats, use default_factory)
# Add a method average() that returns the average grade
# Create 3 students, add grades, and print each average

print("\n#10")
