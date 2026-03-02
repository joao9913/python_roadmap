"""
04_match_case.py
Topic: match-case (Structural Pattern Matching)
Goal: Understand Python's patterns matching (introduced in Python 3.10) and how it differs from if/elif chains
"""

# NOTE: 
# match-case was introduced in Python 3.10.
# It is similar to switch statements in other languages, but much more powerful


# ------------------
# Basic match-case
# ------------------

# Equivalent to simple if/elif comparisons.

day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the work week")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Regular day")
    
# "_" is a wildcard (default case)


# ------------------
# match-case vs if/elif
# ------------------

# Traditional if/elif

value = 2

if value == 1:
    print("One")
elif value == 2:
    print("Two")
else:
    print("Other")

# Equivalent match

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")


# ------------------
# Matching Multiple Values
# ------------------

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 400 | 401 | 403:
        print("Client error")
    case 404:
        print("Not found")
    case _:
        print("Other status")


# ------------------
# Variable Binding
# ------------------

# match can capture values

command = ("move", 10, 20)

match command:
    case ("move", x, y):
        print(f"Moving to {x}, {y}")
    case ("stop,"):
        print("Stopping")
    case _:
        print("Unknown command")
    
# x and y are assigned automatically


# ------------------
# Matching with Conditions (Guards)
# ------------------

number = 15

match number:
    case n if n > 10:
        print("Greater than 10")
    case n:
        print("10 or less")

# "if" inside case is called a guard


# ------------------
# Matching Lists
# ------------------

data = [1, 2, 3]

match data:
    case [1, 2, 3]:
        print("Exact match")
    case [1, *rest]:
        print("Starts with 1, rest: ", rest)
    case _:
        print("Something else")


# ------------------
# Matching Dictionaries
# ------------------

person = {"name": "Joao", "age": 26}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case _:
        print("Unknown structure")


# keys must exist to match


# ------------------
# Nested Pattern Matching
# ------------------

event = ("click", {"x": 100, "y": 200})

match event:
    case ("click", {"x": x, "y": y}):
        print(f"Clicked at {x}, {y}")
    case _:
        print("Unknown event")

    
# ------------------
# Important Differences from if/elif
# ------------------

# 1. match compares patterns, not just equality
# 2. It can destructure data (tuples, list, dicts)
# 3. Order matters - first matching case runs
# 4. No fall-through (unline C-style switch)
# 5. "_" is the default wildcard
# 6. Variables inside patterns are bindings, not comparisons


# ------------------
# Common Mistakes
# ------------------

# 1. Forgetting "_" default case
# 2. Thinking it behaves like C switch (it does not)
# 3. Forgetting Python 3.10+ requirement
# 4. Misunderstanding variable bindind vs equality
# 5. Writing unreachable cases