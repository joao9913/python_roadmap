"""
01_iterators.py
Topic: Iterators
Goal: Understand what iterators are, how iteration works in Python and how to create and use iterators manually.
"""

# ------------------
# What Is An Iterator?
# ------------------

# An iterator is an object that allows you to traverse through a sequence one element at a time
# Iterators follow the Python iterator protocol:
# 1. __iter__() -> returns the iterator object itself
# 2. __next__() -> returns the next value in the sequence

# When there are no more items, __next__() raises StopIteration


# ------------------
# Iterables vs Iterators
# ------------------

# Iterable:
# An object that can be looped over (list, tuple, string, dictionary, set)

numbers = [1, 2, 3]

for num in numbers:
    print(num)

# Behind the scenes Python does this:

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# next(iterator) -> StopIteration


# ------------------
# Using iter() and next()
# ------------------

# iter() creates an iterator from an iterable
# next() retrieves the next item

text = "DOG"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ------------------
# StopIteration
# ------------------

# When the iterator runs out of items, Python raises a StopIteration exception

numbers = [10, 20]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

#print(next(iterator)) # StopIteration


# ------------------
# Iterating Manually
# ------------------

# You can manually control iteration using a loop

numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break


# ------------------
# Creating a Custom Iterator
# ------------------

# To create your own iterator, you define a class that implements __iter__() and __next__()

class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

counter = CountUpTo(5)

for number in counter:
    print(number)


# ------------------
# Iterator vs List
# ------------------

# Lists store all values in memory

numbers = [1, 2, 3, 4 ,5]

# Iterators generate values one at a time

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))


# ------------------
# Built-In Iterators
# ------------------

# Many Python functions return iterators

numbers = [1, 2, 3]

squared = map(lambda x: x ** 2, numbers)

print(next(squared))
print(next(squared))


# ------------------
# Key Concepts
# ------------------

# Iterable:
# Object that can produce an iterator

# Iterator:
# Object that produces values one at a time

# iter(obj):
# Returns an iterator

# next(iterator):
# Returns the next value

# StopIteration:
# Exception raised when iteration ends


# ------------------
# When Iterators Are Useful
# ------------------

# Iterators are important for:

# large datasets
# streaming data
# generators
# file reading
# memory-efficient loops


# ------------------
# Summary
# ------------------

# Iterables produce iterators
# Iterators produce values one at a time
# next() retrieves the next value
# StopIteration signals the end
# Python for-loops use iterators internally
