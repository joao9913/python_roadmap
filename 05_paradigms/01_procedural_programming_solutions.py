# 01_procedural_programming_exercises.py
"""
Exercises for Procedural Programming in Python.
Focus on writing functions, modular programs, and using global/local variables.
"""

# ------------------
# Basic Function Usage
# ------------------

# 1. Write a function greet() that prints "Hello!" and call it.
# Then call it again with a different message.

print("#1")

def greet(message):
    print(message)

greet("Hello")
greet("Good morning")

print()

# 2. Write a function add(a, b) that returns the sum of two numbers.
# Call it with numbers 5 and 7 and print the result.

print("#2")

def add(a, b):
    return a + b

print(add(5, 7))

print()

# 3. Write a function multiply(a, b) that returns the product of two numbers.
# Call it and print the result.

print("#3")

def multiply(a, b):
    return a * b

print(multiply(2, 3))

print()

# 4. Write a function say_name(name) that prints "Your name is <name>".
# Call it with your name.

print("#4")

def say_name(name):
    print(f"Your name is {name}")

say_name("João")

print()

# ------------------
# Parameters and Return Values
# ------------------

# 5. Write a function square(n) that returns the square of a number.
# Test it with multiple values.

print("#5")

def square(n):
    return n ** 2

print(square(2))

print()

# 6. Write a function average(numbers) that takes a list of numbers and returns the average.

print("#6")

def average(numbers):
    sum_total = 0
    for num in numbers:
        sum_total += num

    return sum_total/len(numbers)

numbers = [1, 2, 3]
print(average(numbers))

print()

# 7. Write a function is_even(n) that returns True if n is even, False otherwise.
# Test it with multiple numbers.

print("#7")

def is_even(n):
    return n % 2 == 0

print(is_even(3))

print()

# ------------------
# Control Flow Inside Functions
# ------------------

# 8. Write a function largest(a, b, c) that returns the largest of three numbers.

print("#8")

def largest(a, b, c):
    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest

print(largest(5, 4, 3))

print()

# 9. Write a function factorial(n) that returns n! using a for loop.

print("#9")

def factorial(n):
    previous = 1
    for i in range(1, n+1):
        previous = previous * i

    return previous

print(factorial(4))

print()

# 10. Write a function count_vowels(text) that returns the number of vowels in a string.

print("#10")

def count_vowels(text):
    vowels = "aeiou"
    total = 0

    for char in text:
        total += 1 if char.lower() in vowels else 0

    return total

print(count_vowels("aaabbb"))

print()

# ------------------
# Modular Programming
# ------------------

# 11. Write a function get_input() that asks the user for a number and returns it.
# Write a function double_number(n) that returns n*2.
# Write a main() function that gets a number, doubles it, and prints it.
# Call main().

print("#11")

def get_input():
    return int(input("Enter a number: "))

def double_number(n):
    return n * 2

def main():
    print(double_number(get_input()))

#main()

print()

# 12. Create a small calculator with functions:
# add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# Call each function and print results.

print("#20")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main(a, b):
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))

main(4, 8)

print()

# 13. Write a function process_list(numbers) that:
# - Prints even numbers
# - Prints odd numbers separately
# Test it with a list of numbers.

print("#13")

def process_list(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print(even_numbers)
    print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6]

process_list(numbers)

print()

# ------------------
# Global vs Local Variables
# ------------------

# 14. Create a global variable x = 10
# Write a function that prints x
# Then modify x inside the function without 'global' keyword and print it
# Observe the difference

print("#14")

x = 10

def print_x():
    x = 15
    print(x)

print_x()
print(x)

print()

# 15. Modify the previous function to use the 'global' keyword and increment x by 5
# Print x inside and outside the function

print("#15")

x = 10

def print_x():
    global x
    x += 5
    print(x)

print_x()
print(x)

print()

# ------------------
# Loops and Functions
# ------------------

# 16. Write a function print_numbers(n) that prints numbers from 1 to n using a for loop.

print("#16")

def print_numbers(n):
    for i in range(n):
        print(i + 1)

print_numbers(10)

print()

# 17. Write a function sum_numbers(n) that returns the sum of numbers from 1 to n using a loop.

print("#17")

def sum_numbers(n):
    sum_total = 0

    for num in range(1, n+1):
        sum_total += num

    return sum_total

print(sum_numbers(5))

print()

# 18. Write a function primes_up_to(n) that returns a list of all prime numbers up to n.

print("#18")

def primes_up_to(n):
    list_primes = []

    for num in range(n):
        if num > 1:
            for i in range(2, num):
                if num % i != 0:
                    list_primes.append(num)
                    break


    return list_primes

print(primes_up_to(30))

print()

# ------------------
# Combining Ideas
# ------------------

# 19. Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.

print("#19")

def fibonacci(n):
    list_fib = []

    for num in range(n):
        if num <= 1:
            list_fib.append(num)
            continue

        number = list_fib[num - 1] + list_fib[num - 2]
        list_fib.append(number)

    return list_fib

print(fibonacci(8))

print()

# 20. Write a function modular_program() that:
# - Asks the user for a list of numbers (comma separated)
# - Calculates and prints the sum
# - Calculates and prints the average
# - Prints the even numbers
# - Uses at least 3 separate functions for input, processing, and printing

print("#20")

def sum_numbers(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

def average_numbers(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)

def even_numbers(numbers):
    even_numbers_list = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers_list.append(num)

    return even_numbers_list

def output_functions(total_sum, average_nums, even_nums):
    print(f"Sum: {total_sum}")
    print(f"Average: {average_nums}")
    print(f"Even numbers: {even_nums}")

def modular_program():
    list_numbers = [int(x) for x in input("Enter a list of numbers: ").split(",")]

    total_sum = sum_numbers(list_numbers)
    averages = average_numbers(list_numbers)
    even_numbers_list = even_numbers(list_numbers)

    output_functions(total_sum, averages, even_numbers_list)

modular_program()

print()
