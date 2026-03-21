"""
02_singleton.py
Topic:
Goal:
"""

# ------------------
# Concept
# ------------------

# The Singleton pattern ensures:
# - A class has ONLY one instance
# - That instance is globally accessible

# ------------------
# Why This Pattern Exists
# ------------------

# 1. Centralized State
#   - One source of truth (e.g. config, cache)

# 2. Resource Control
#   - Avoid creating expensive objects multiple times (DB connections)

# 3. Consistency
#   - All parts of the system use the same instance


# ------------------
# Implementation (Metaclass Approach)
# ------------------

# We use a metaclass to control how instances are created

class SingletonMeta(type):
    _instances = {} # Stores one instance per class

    def __call__(cls, *args, **kwargs):
        # This is triggered when we do: MyClass()

        if cls not in cls._instances:
            # Create instance only once
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class Singleton(metaclass = SingletonMeta):
    def __init__(self, value):
        self.value = value

# First call:
s1 = Singleton(10)
# - SingletonMeta.__call__ runs
# - No instance exists -> create one
# - __init__ runs -> value = 10
# - Instance stores in _instances

# Second call:
s2 = Singleton(20)
# - SingletonMeta.__call__ runs again
# - Instance already exists -> return it
# - __init__ is NOT called again

print(s1.value) # 10
print(s2.value) # 10 (same instance)

# s1 and s2 reference the SAME object


# ------------------
# Verification
# ------------------

print(s1 is s2) # True


# ------------------
# Alternative (Simpler Pythonic Approach)
# -----------------

# In Python, you often don't need a full Singleton pattern
# A module itself behaves like a singleton

# Example
# config.py
#   value = 10

# main.py
#   import config
#   print(config.value)

# Already shared globally


# ------------------
# When To Use Singleton
# ------------------

# - Configuration manager
# - Logging system
# - Cache manager
# - Database connection handler
# - Thread pools

# Use it when:
# - You truly need ONE instance across the entire app


# ------------------
# When NOT To Use Singleton
# ------------------

# - When you just want "easy access" (use dependency injection instead)
# - When it hides dependencies (bad for testing)
# - When multiple instances might be needed later

# Singleton introduces GLOBAL STATE -> this can make debugging harder


# ------------------
# Key Takeaways
# ------------------

# - Singleton controls instance creation
# - Metaclasses allow intercepting instantiation
# - Python often doesn't need strict Singleton patterns
# - Use carefully - global state is risky
