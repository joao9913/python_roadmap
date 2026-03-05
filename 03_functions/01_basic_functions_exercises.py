# ------------------
# Basic Functions Definition
# ------------------

# 1. Create a function called say_hello
# The function should print "Hello, world!"
# Then call the function

def say_hello():
    print("Hello, world!")

say_hello()


# ------------------
# Function With Parameter
# ------------------

# 2. Create a function greet(name)
# It should print "Hello <name>"
# Call the function with:
# "Ana"
# "Carlos"

def greet(name):
    print(f"Hello {name}")

greet("Ana")
greet("Carlos")


# ------------------
# Multiple Parameters
# ------------------

# 3. Create a function add_numbers(a, b)
# It should print the sum of the two numbers
# Call the function with:
# 5 and 7

def add_numbers(a, b):
    print(a + b)

add_numbers(5, 7)


# ------------------
# Return Values
# ------------------

# 4. Create a function multiply(a, b)
# The function should return the multiplication result
# Store the result in a variable and print it

def multiply(a, b):
    return a * b

multi_res = multiply(2, 3)
print(multi_res)


# ------------------
# Using Return In Calculations
# ------------------

# 5. Create a function square(number)
# Return the square of the number
# Call the function and print the result + 10

def square(number):
    return number ** 2

print(square(2) + 10)


# ------------------
# Default Parameters
# ------------------

# 6. Create a function welcome_user(name="Guest")
# It should print: "Welcome <name>"
# Call it:
# - without arguments
# - with "Joao"

def welcome_user(name="Guest"):
    print(f"Welcome {name}")

welcome_user()
welcome_user("Joao")


# ------------------
# Keyword Arguments
# ------------------

# 7. Create a function describe_person(name, age, country)
# Print:
# "<name> is <age> years old and lives in <country>"
# Call the function using keyword arguments
# Change the order of the arguments when calling

def describe_person(name, age, country):
    print(f"{name} is {age} years old and lives in {country}")

describe_person(name = "Joao", age = 26, country = "portugal")
describe_person(age = 26, name = "Joao", country = "F")


# ------------------
# Returning Multiple Values
# ------------------

# 8. Create a function get_min_max(numbers)
# It should return:
# - the smaller number
# - the largest number
# Use the list:
numbers = [4, 7, 2, 9, 1]

# Unpack the result into two variables and print them
def get_min_max(numbers):
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        elif number < min_number:
            min_number = number
    
    return min_number, max_number

min_num, max_num = get_min_max(numbers)
print(min_num, max_num)


# ------------------
# Function Composition
# ------------------

# 9. Create two functions:
# double(n)
# Returns n * 2

# add_five(n)
# Returns n + 5

# Create a third function process(n)
# It should:
# - double the number
# - then add five
# Return the final result
# Call process (10) and print the results

def double(n):
    return n * 2

def add_five(n):
    return n + 5

def process(n):
    return add_five(double(n))

print(process(10))


# ------------------
# Local Scope
# ------------------

# 10. Inside a function create a variable called message
# Print the variable inside the function
# Try printing it outside the function
# Observe the error

def function_1():
    message = ""
    print(message)

#print(message)
# the variable can only be accessed inside the scope its declared on


# ------------------
# Global Variable Access
# ------------------

# 11. Create a global variable:
discount = 10

# Create a function show_discount()
# It should print the value of discount

def show_discount():
    print(discount)

show_discount()


# ------------------
# Simple Calculator Function
# ------------------

# 12. Create a function calculate(a, b, operation)

# operations can be:
# "add"
# "substract"
# "multiply"
# "divide"

# The function should return the correct result

# Example calls:
# calculate(10, 5, "add")
# calculate(10, 5, "multiply")

def calculate(a, b, operation):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b
        case _:
            raise ValueError("Invalid operation")

print(calculate(4, 2, "add"))

# ------------------
# Even/Odd Checker
# ------------------

# 13. Create a function is_even(number)

# Return True if number is even
# Return False otherwise
# Test it with several numbers

def is_even(number):
    return number % 2 == 0
    
print(is_even(2))


# ------------------
# String Processing
# ------------------

# 14. Create a function count_vowels(text)
# Count how many vowels exist in the string
# vowels: a, e, i, o, u
# Return the count

def count_vowels(text):
    vowels = 0
    for char in text.lower():
        if char in "aeiou":
            vowels += 1
    
    return vowels

print(count_vowels("aajj"))


# ------------------
# Function That Calls Another Function
# ------------------

# 15. Create two functions:
# area_rectangle(width, height)
# Returns width * height

# print_area(width, height)
# Calls area_rectangle and prints:
# "Area is <result>"

# Call print_area(5, 8)

def area_rectangle(width, height):
    return width * height

def print_area(width, height):
    print(f"Area is {area_rectangle(width, height)}")

print_area(5, 8)


# ------------------
# Manual Max Function
# ------------------

# 16. Create a function find_max(numbers)
# Find the maximum value WITHOUT using max()
# Return the maximum

numbers = [3, 17, 5, 22, 9]

def find_max(numbers):
    max_number = numbers[0]

    for num in numbers[1:]:
        if num > max_number:
            max_number = num
        
    return max_number

print(find_max(numbers))


# ------------------
# Bonus Challenge
# ------------------

# 17. Create a function login(username, password)

# Correct credentials:
# username = "admin"
# password = "1234"

# If correct -> return "Login successful"
# Otherwise -> return "Invalid credentials"

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid credentials"

print(login("admin", "1234"))