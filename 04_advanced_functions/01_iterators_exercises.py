# ------------------
# Basic Iterator Usage
# ------------------

# 1. Given the list below:
numbers = [10, 20, 30]

# Create an iterator using iter()
# Use next() to print each element manually


print("#1")

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # Would return StopIteration exception

print()


# 2. Given the string:
text = "PYTHON"

# Create an iterator from the string
# Print the first three characters using next()


print("#2")

iterator = iter(text)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print()


# 3. Create a list:
values = [5, 15, 25, 35]

# Create an iterator
# Print two elements using next()
# Then print the remaining elements using a for loop

print("#4")

iterator = iter(values)
print(next(iterator))
print(next(iterator))

for num in iterator:
    print(num)

print()


# ------------------
# Understanding StopIteration
# ------------------

# 4. Create a list with two elements

print("#4")

numbers = [1, 2]

# Use iter() and next() to retrieve both elements

iterator = iter(values)
print(next(iterator))
print(next(iterator))

# Try calling next() again and observe the StopIteration error

# print(next(iterator)) # will throw StopIteration error

print()


# 5. Rewrite the previous exercise using try/except
# Catch the StopIteration exception and print:
# "Iterator finished"

print("#5")

numbers = [2, 3]

try:
    iterator = iter(numbers)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Iterator finished")

print()


# ------------------
# Manual Iteration Loop
# ------------------

# 6. Given the list:
numbers = [1, 2, 3, 4]

# Create an iterator
# Use a while True loop with try/except
# Manually print all elements using next()

print("#6")

iterator = iter(numbers)
while True:
    try:
        print(next(iterator))

    except StopIteration:
        break

print()

# ------------------
# Iterators With Built-in Functions
# ------------------

# 7. Given:
numbers = [1, 2, 3, 4]

# Use map() to create an iterator that squares the numbers
# Use next() to print the first two results

print("#7")

iterator = iter(map(lambda x: x ** 2, numbers))
print(next(iterator))
print(next(iterator))

print()

# 8. Given:
numbers = [10, 15, 20, 25]

# Use filter() to create an iterator that keeps only numbers > 15
# Convert the iterator to a list and print it

print("#8")

iterator = list(iter(filter(lambda x: x > 15, numbers)))
print(iterator)

print()


# ------------------
# Creating a Custom Iterator
# ------------------

# 9. Create a class CountDown
# The iterator should count down from a starting number to 1
#
# Example:
# CountDown(5)
# Output:
# 5
# 4
# 3
# 2
# 1

print("#9")

class CountDown():
    def __init__(self, starting_num):
        self.starting_num = starting_num
        self.current = starting_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value

counter = CountDown(5)
for number in counter:
    print(number)

print()


# 10. Create a class EvenNumbers
# The iterator should generate even numbers from 0 up to a limit
#
# Example:
# EvenNumbers(10)
# Output:
# 0, 2, 4, 6, 8, 10

print("#10")

class EvenNumbers():
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current % 2 != 0:
            self.current += 1

        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

counter_even = EvenNumbers(10)
for num in counter_even:
    print(num)

print()


# ------------------
# More Control Over Iteration
# ------------------

# 11. Create a class StepCounter
# It should count from a start value to a limit
# increasing by a custom step.
#
# Example:
# StepCounter(start=0, step=3, limit=12)
# Output:
# 0, 3, 6, 9, 12

print("#11")

class StepCounter():
    def __init__(self, start, step, limit):
        self.limit = limit
        self.start = start
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value

step_counter = StepCounter(3, 3, 14)

for step in step_counter:
    print(step)

print()

# ------------------
# Thinking Like Python
# ------------------

# 12. Create an iterator class ReverseList
# It should iterate through a list in reverse order.
#
# Example:
# ReverseList([1, 2, 3])
# Output:
# 3, 2, 1

print("#12")

class ReverseList:
    def __init__(self, list_numbers):
        self.list_numbers = list_numbers
        self.current = len(list_numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        value = self.list_numbers[self.current]
        self.current -= 1
        return value

numbers = [1, 2, 3]

reverse_list = ReverseList(numbers)

for num in reverse_list:
    print(num)

print()


# ------------------
# Iterator State
# ------------------

# 13. Create a class RepeatValue
# It should repeat a given value a specific number of times.
#
# Example:
# RepeatValue("A", 3)
# Output:
# A, A, A

print("#13")

class RepeatValue():
    def __init__(self, value, counter):
        self.value = value
        self.counter = counter
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.counter:
            raise StopIteration

        self.current += 1
        return self.value

repeat_value = RepeatValue("A", 5)

for value in repeat_value:
    print(value)

print()


# ------------------
# Combining Ideas
# ------------------

# 14. Create a class FibonacciIterator
# It should generate the Fibonacci sequence up to n numbers.
#
# Example:
# FibonacciIterator(7)
# Output:
# 0, 1, 1, 2, 3, 5, 8

print("#14")

class FibonacciIterator():
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

print()


# ------------------
# Bonus Challenge
# ------------------

# 15. Create a class RangeLike
# Implement your own version of Python's range().
#
# It should support:
# start
# stop
# step
#
# Example:
# RangeLike(2, 10, 2)
# Output:
# 2, 4, 6, 8
#
# Use the iterator protocol (__iter__ and __next__)
