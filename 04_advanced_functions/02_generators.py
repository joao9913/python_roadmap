"""
02_generators.py
Topic: Generators
Goal: Understand what generators are, how they differ from iterators and how to create memory efficient sequences
"""

# ------------------
# What Is A Generator
# ------------------

# A generator is a special type of iterator that produces values one at a time
# instead of storing the entire sequence in memory

# Generators use the keyword "yield" instead of "return"

# Each time the generator is asked for a value, it pauses execution,
# returns the value, and resumes from the same point later.

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# ------------------
# Yield vs Return
# ------------------

# return -> exists the function completely
# yield -> pauses the function and saves its state

def test_return():
    return 1
    return 2

print(test_return())

def test_yield():
    yield 1
    yield 2

g = test_yield()

print(next(g))
print(next(g))


# ------------------
# Generators Are Iterators
# ------------------

# Generators automatically implement the iterator protocol:
# __iter__()
# __next__()

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

for num in gen:
    print(num)


# ------------------
# Generator Execution Flow
# ------------------

# A generator only runs when next() is called

def flow():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

g = flow()

print(next(g))
print(next(g))
print(next(g))


# ------------------
# Generators With Loops
# ------------------

# Generators are often used with loops to produce sequences dynamically

def count_up_to(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1

counter = count_up_to(5)

for value in counter:
    print(value)


# ------------------
# Memory Efficiency
# ------------------

# Lists store all values in memory

numbers_list = [x for x in range(1_000_000)]

# Generators produce values one at a time

numbers_gen = (x for x in range(1_000_000))

print(type(numbers))
print(type(numbers_gen))


# ------------------
# Generators vs Iterator Class
# ------------------

# Generator version (simples)

def count(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

for n in count(5):
    print(n)

# Equivalent iterator class (more verbose)

class CountIterator:

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

for n in CountIterator(5):
    print(n)


# ------------------
# Infinite Generators
# ------------------

# Generators can create infinite sequences.

def infinite_counter():
    num = 1

    while True:
        yield num
        num += 1

counter = infinite_counter()

print(next(counter))
print(next(counter))


# ------------------
# Generators With Large Data
# ------------------

# Generators are useful when working with large datasets

def read_lines_simulated():
    for i in range(1_000_000):
        yield f"Line {i}"

gen = read_lines_simulated()

print(next(gen))
print(next(gen))


# ------------------
# Key Concepts
# ------------------

# Generator:
# Function that yields one value at a time

# yield
# Pauses execution and returns a value

# next(generator)
# Resumes execution until the next yield

# StopIteration
# Raised when the generator finishes


# ------------------
# When Generators Are Useful
# ------------------

# Generators are importat for:

# large datasets
# streaming data
# infinite sequences
# pipelines
# file processing
# memory optimization


# ------------------
# Summary
# ------------------

# Generators are a simpler way to create iterators
# They use "yield" instead of returning all values at once
# Execution pauses after each yield
# They are memory-efficient
# They are ideal for large of infinite data streams
