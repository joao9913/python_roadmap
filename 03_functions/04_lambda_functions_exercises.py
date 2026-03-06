# ------------------
# Basic Lambda
# ------------------

# 1. Create a lambda function that adds two numbers
# Store it in a variable called add
# Print the result of add(5, 3)

add = lambda x, y : x + y
print(add(5, 3))


# 2. Create a lambda function that returns the square of a number.
# Store it in a variable called square.
# Print it

square = lambda x: x ** 2
print(square(4))

# ------------------
# Lambda Returning Boolean
# ------------------

# 3. Create a lambda function is_even.
# Return True if a number is even, otherwise False.
# Test it with several numbers.

is_even = lambda x: x % 2 == 0
print(is_even(2))


# 4. Create a lambda function is_positive.
# Return True if a number is greater than 0.
# Test it with both positive and negative numbers.

is_positive = lambda x: x > 0
print(is_positive(-1))


# ------------------
# Lambda With map()
# ------------------

# 5. Given:
numbers = [1, 2, 3, 4, 5]

# Use map() with lambda to create a list of squares.
# Print the result.

squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# 6. Given:
numbers = [10, 20, 30, 40]

# Use map() with lambda to create a list where each number is multiplied by 3.
# Print the result.

multiplied = list(map(lambda x: x * 3, numbers))
print(multiplied)

# ------------------
# Lambda With filter()
# ------------------

# 7. Given:
numbers = [1, 2, 3, 4, 5, 6]

# Use filter() with lambda to keep only even numbers.
# Convert the result to a list and print it.

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 8. Given:
numbers = [10, 15, 20, 25, 30]

# Use filter() with lambda to keep numbers greater than 20.
# Convert the result to a list and print it.

greater_20 = list(filter(lambda x: x > 20, numbers))
print(greater_20)


# ------------------
# Lambda With sorted()
# ------------------

# 9. Given:
numbers = [5, 1, 8, 3, 2]

# Sort the list using sorted() with a lambda as the key.
# Print the sorted list.

sorted_numbers = sorted(numbers, key = lambda x: x)
print(sorted_numbers)


# 10. Given:
words = ["banana", "apple", "cherry", "kiwi"]

# Sort the list by word length using lambda.
# Print the result.

sorted_length = list(sorted(words, key=lambda words: len(words)))
print(sorted_length)

# ------------------
# Sorting Dictionaries
# ------------------

# 11. Given:
people = [
    {"name": "Ana", "age": 25},
    {"name": "Carlos", "age": 30},
    {"name": "Bruno", "age": 20}
]

# Sort the list by age using lambda.
# Print the result.

sorted_age = list(sorted(people, key=lambda person: person["age"]))
print(sorted_age)


# 12. Sort the same list by name using lambda.
# Print the result.

sorted_name = list(sorted(people, key = lambda person: person["name"]))
print(sorted_name)


# ------------------
# Using Lambda Inside Functions
# ------------------

# 13. Create a function apply_operation(a, b, operation).
# operation will be a lambda function.
# The function should return operation(a, b).

def apply_operation(a, b, operation):
    return operation(a, b)

result = apply_operation(5, 3, lambda x, y : x * y)
print(result)


# 14. Call apply_operation with a lambda that adds two numbers.
# Print the result.

result = apply_operation(4, 3, lambda x, y: x + y)
print(result)


# 15. Call apply_operation again but multiply the numbers using lambda.
# Print the result.

result = apply_operation(5, 5, lambda x, y: x * y)
print(result)


# ------------------
# Combining map and filter
# ------------------

# 16. Given:
numbers = [1, 2, 3, 4, 5, 6]

# First filter only even numbers using lambda.
# Then square them using map().
# Print the final list.

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_list = list(map(lambda x: x ** 2, even_numbers))
print(squared_list)

# ------------------
# Lambda Returning Tuples
# ------------------

# 17. Given:
numbers = [1, 2, 3, 4, 5]

# Use map() with lambda to create tuples (number, number^2).
# Print the result.

tuples = list(map(lambda x: (x, x**2), numbers))
print(tuples)


# ------------------
# Real World Thinking
# ------------------

# 18. Given:
prices = [100, 200, 300]

# Use map() with lambda to add 23% tax to each price.
# Print the new list.

tax_list = list(map(lambda x: x * 1.23, prices))
print(tax_list)


# 19. Given:
words = ["apple", "banana", "kiwi", "pear"]

# Use filter() with lambda to keep words longer than 4 characters.
# Print the result.

long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)


# ------------------
# Bonus Challenge
# ------------------

# 20. Create a lambda that returns:
# "Even" if the number is even
# "Odd" otherwise
# Test it with several numbers.

number = 1

even_or_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(even_or_odd(number))
