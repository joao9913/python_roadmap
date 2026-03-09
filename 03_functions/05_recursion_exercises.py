# ------------------
# Basic Recursion
# ------------------

# 1. Create a function countdown(n)
# Print numbers from n down to 1
# When it reaches 0, print "Done"

def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        countdown(n - 1)

print("#1")
countdown(5)
print("")

# 2. Create a function countup(n)
# Print numbers from 1 up to n using recursion

def countup(n):
    if n == 1:
        print(1)
        return
    else:
        countup(n - 1)
        print(n)

print("#2")
countup(5)
print("")


# 3. Create a function print_numbers(n)
# Print numbers from n down to 0

def print_numbers(n):
    if n == 0:
        print(n)
        return
    else:
        print(n)
        print_numbers(n - 1)

print("#3")
print_numbers(5)
print("")

# ------------------
# Mathematical Recursion
# ------------------

# 4. Create a function factorial(n)
# Return the factorial of n
# Example: factorial(5) -> 120
# 1 x 2 x 3 x 4 x 5 = 120

def factorial(n):
    if n == 1 or n == 2:
        return n

    return n * factorial(n - 1)

print("#4")
print(factorial(5))
print("")

# 5. Create a function recursive_sum(n)
# Return the sum of numbers from 1 to n
# Example: recursive_sum(5) -> 15
# 1 + 2 + 3 + 4 + 5 = 15

def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)

print("#5")
print(recursive_sum(5))
print()


# 6. Create a function power(base, exponent)
# Return base^exponent using recursion
# Example: power(2, 3) -> 8
# 2 x 2 x 2 = 8

def power(base, exponent):
    if exponent == 1 or base == 1:
        return base

    return base * power(base, exponent - 1)


print("#6")
print(power(2, 3))
print()

# ------------------
# Fibonacci
# ------------------

# 7. Create a function fibonacci(n)
# Return the nth Fibonacci number
# Sequence: 0, 1, 1, 2, 3, 5, 8...
# fibonacci(7) = 7

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("#7")
print(fibonacci(6))
print()


# 8. Create a function print_fibonacci(n)
# Print the first n Fibonacci numbers

def print_fibonacci(n):
    for i in range(n+1):
        print(fibonacci(i))

print("#8")
print_fibonacci(6)
print()

# ------------------
# Recursion With Strings
# ------------------

# 9. Create a function reverse_string(text)
# Return the reversed string using recursion
# Example: "hello" -> "olleh"

def reverse_string(text):
    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]

print("#9")
print(reverse_string("dog"))
print()


# 10. Create a function count_characters(text)
# Return the number of characters in a string using recursion

def count_characters(text):
    if text == "":
        return 0

    return 1 + count_characters(text[1:])

print("#10")
print(count_characters("dog"))
print()

# ------------------
# Recursion With Lists
# ------------------

# 11. Create a function sum_list(numbers)
# Return the sum of all numbers in a list using recursion

def sum_list(numbers):
    if numbers == []:
        return 0

    return numbers[0] + sum_list(numbers[1:])

numbers = [1, 2, 3]

print("#11")
print(sum_list(numbers))
print()


# 12. Create a function find_max(numbers)
# Return the largest number in a list using recursion

def find_max(numbers):
    if numbers == []:
        return 0

    return numbers[0] if numbers[0] > find_max(numbers[1:]) else find_max(numbers[1:])

print("#12")
print(find_max(numbers))
print()


# 13. Create a function count_elements(numbers)
# Return how many elements are in the list using recursion

def count_elements(numbers):
    if numbers == []:
        return 0

    return 1 + count_elements(numbers[1:])

print("#13")
print(count_elements(numbers))
print()


# ------------------
# Filtering With Recursion
# ------------------

# 14. Create a function sum_even(numbers)
# Return the sum of all even numbers in a list using recursion

def sum_even(numbers):
    if numbers == []:
        return 0

    return numbers[0] + sum_even(numbers[1:]) if numbers[0] % 2 == 0 else sum_even(numbers[1:])

numbers = [1, 2, 2, 3, 2]

print("#14")
print(sum_even(numbers))
print()


# 15. Create a function count_positive(numbers)
# Return how many positive numbers are in the list

def count_positive(numbers):
    if numbers == []:
        return 0

    return 1 + count_positive(numbers[1:]) if numbers[0] > 0 else count_positive(numbers[1:])

numbers = [1, 1, -1, -1, 1]

print("#15")
print(count_positive(numbers))
print()


# ------------------
# Practical Recursion
# ------------------

# 16. Create a function multiply_list(numbers)
# Return the product of all numbers in the list
# Example: [2,3,4] -> 24

def multiply_list(numbers):
    if numbers == []:
        return numbers[0]
    elif len(numbers) == 1:
        return numbers[0]

    return numbers[0] * multiply_list(numbers[1:])

numbers = [2, 3, 4] # = 2 x 3 x 4 = 24

print("#16")
print(multiply_list(numbers))
print()


# 17. Create a function remove_first(text)
# Recursively remove the first character until the string is empty
# Print each step

def remove_first(text):
    if text == "":
        print("")
    else:
        print(text)
        remove_first(text[1:])


print("#17")
remove_first("dog")
print()


# ------------------
# Slightly Harder
# ------------------

# 18. Create a function is_palindrome(text)
# Return True if the string is a palindrome
# Example: "radar" -> True

def is_palindrome(text):
    if text == "" or len(text) == 1:
        return True

    first_letter = text[0]
    last_letter = text[len(text)-1]

    return False if first_letter != last_letter else is_palindrome(text[1:-1])

text = "raat"

print("#18")
print(is_palindrome(text))
print()


# 19. Create a function flatten_list(nested_list)
# Example:
# [1, [2, 3], [4, [5]]] -> [1, 2, 3, 4, 5]


# ------------------
# Bonus Challenge
# ------------------

# 20. Create a function count_occurrences(numbers, target)
# Return how many times target appears in the list
