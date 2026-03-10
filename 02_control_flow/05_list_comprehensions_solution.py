# ------------------
# Basic Creation
# ------------------

# 1. Create a list of numbers from 1 to 10 using list comprehension

numbers = [i for i in range(1, 11)]
print(numbers)

# 2. Create a list of squares from 1 to 10

squares = [i ** 2 for i in range(1, 11)]
print(squares)

# 3. Create a list of numbers from 1 to 20 that are divisible by 3

div_numbers = [i for i in range(1, 21) if i % 3 == 0]
print(div_numbers)


# ------------------
# Working With Strings
# ------------------

# 4. Given:

words = ["apple", "banana", "cherry", "kiwi"]

# Create a list with the length of each word

list_len = [len(l) for l in words]
print(list_len)

# 5. From the same list, create a new list containing only words with more than 5 letters

new_list = [word for word in words if len(word) > 5]
print(new_list)

# 6. Create a list with all words converted to uppercase

upper_list = [word.upper() for word in words]
print(upper_list)


# ------------------
# If-Else Inside Comprehension
# ------------------

# 7. Create a list from 1 to 10 where:
# - Even numbers become "Even"
# - Odd numbers become "Odd"

even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(even_odd_list)

# 8. Given
numbers = [10, 15, 20, 25, 30]

# Create a list where:
# - If number > 20 -> "High"
# - Otherwise -> "Low"

num_list = ["High" if num > 20 else "Low" for num in numbers]
print(num_list)


# ------------------
# Nested Comprehension
# ------------------

# 9. Given:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Flatten this matrix into a single list.

matrix_list = [num for row in matrix for num in row]
print(matrix_list)

# 10. Create a list of all pairs (x, y)
# where x is from 1 to 3
# and y is from 1 to 2

pairs_list = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print(pairs_list)

# Wrong


# ------------------
# Multiple Conditions
# ------------------

# 11. Create a list of numbers from 1 to 50
# that are divisible by both 2 and 5

divisible = [i for i in range (1, 51) if i % 2 == 0 and i % 5 == 0]
print(divisible)

# 12. Create a list of numbers from 1 to 30
# that are divisible by 3 but NOT divisible by 2

divisible = [i for i in range(1, 31) if i % 3 == 0 and i % 2 != 0]
print(divisible)


# ------------------
# Dictionary Comprehension
# ------------------

# 13. Create a dictionary where:
# - Keys are numbers from 1 to 5
# - Values are the square of each number
dict = {x: x ** 2 for x in range(1, 6)}
print(dict)

# 14. Given:
names = ["Ana", "Joao", "Carlos"]

# Create a dictionary where:
# - Key is the name
# - Value is the length of the name

dict = {name: len(name) for name in names}
print(dict)


# ------------------
# Sets Comprehension
# ------------------

# 15. Given:
numbers = [1, 2, 2, 3, 4, 4, 5]

# Create a set of unique squared values
unique_squared = {x ** 2 for x in numbers}
print(unique_squared)


# ------------------
# Advanced Thinking
# ------------------

# 16. Given:
values = [1, -2, 3, -4, 5]

# Create a list with absolute values of each number
abs_values = [abs(i) for i in values]
print(abs_values)


# 17. Create a list of all lowercase letters
# from the string "Hello World"
# (ignore spaces)

lower_letters = [l.lower() for l in "Hello World" if l != " "]
print(lower_letters)

# 18. Create a list of tuples (number, square)
# for numbers from 1 to 10

list_tuples = [(x, x**2) for x in range(1, 11)]
print(list_tuples)


# 19. Given:
numbers = [1, 2, 3, 4, 5, 6]

# Create a list containing only numbers greater than 3 but multiplied by 10
new_list = [i*10 for i in numbers if i > 3]
print(new_list)


# 20. Bonus:
# Create a 3x3 multiplication table as a nested list using list comprehension
# Expected structure:
# [
#   [1, 2, 3],
#   [2, 4, 6],
#   [3, 6, 9]
# ]

multi_table = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(multi_table)