# ------------------
# Basic *args
# ------------------

# 1. Create a function print_numbers(*args)
# Print all numbers received

# Example call:
# print_numbers(1, 2, 3, 4)

def print_numbers(*args):
    # print(args)   # if you want to print the tuple from *args

    # if you want to print each individual number
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)

# 2. Create a function sum_all(*args)
# Return the sum of all numbers passed

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    
    return total

print(sum_all(1, 2, 3))


# 3. Create a function find_max(args)
# Return the largest number

def find_max(*args):
    max_value = args[0]

    for num in args:
        if num > max_value:
            max_value = num
    
    return max_value

print(find_max(1, 5, 2))


# ------------------
# Iterating *args
# ------------------

# 4. Create a function print_words(*args)
# Print each word on a new line

def print_words(*args):
    for word in args:
        print(word)
    
print_words("apple", "banana", "cherry")


# 5. Create a function count_arguments(*args)
# Return how many arguments were passed

def count_arguments(*args):
    return len(args)

print(count_arguments(1, 2, 3, 4))


# ------------------
# Mixing Parameters and *args
# ------------------

# 6. Create a function introduce (name, *hobbies)
# Print:
# "Name: <name>"
# Then print each hobby

def introduce(name, *hobbies):
    print(f"Name: {name}")
    
    for hobby in hobbies:
        print(hobby)

introduce("Ana", "Skating", "Gym", "Guitar Playing")

# 7. Create a function multiply_all(multiplier, *numbers)
# Multiply each number by multiplier
# Print each result

def multiply_all(multiplier, *numbers):
    for num in numbers:
        print(num * multiplier)

multiply_all(2, 3, 4, 5)


# ------------------
# Basic **kwargs
# ------------------

# 8. Create a function print_user(**kwargs)
# print the dictionary received

def print_user(**kwargs):
    print(kwargs)

print_user(name="Ana", age = 25, country = "Portugal")


# 9. Create a function show_profile(**kwargs)
# Print each key and value in the format:
# key : value

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_profile(name="Carlos", role="Admin", active=True)

# 10. Create a function count_keys(**kwargs)
# Return how many keyword arguments were passed

def count_keys(**kwargs):
    key_count = 0

    for key in kwargs.keys():
        key_count += 1
    
    return key_count

print(count_keys(a=1, b=2, c=3))


# ------------------
# Combining *args and **kwargs
# ------------------

# 11. Create a function show_data(*args, **kwargs)

# Print:
# "Positional:" followed by args
# "Keyword:" followed by kwargs

def show_data(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

show_data(1, 2, 3, name="Ana", age=25)

# 12. Create a function logger(level, *messages)

# Print:
# Level: <level>
# Then print all messages

def logger(level, *messages):
    print(f"LEVEL: {level}")

    for msg in messages:
        print(f"Message: {msg}")

logger("INFO", "User login", "Session started")


# ------------------
# Argument Unpacking
# ------------------

# 13. Create a function add_three(a, b, c)
# Return their sum

def add_three(a, b, c):
    return a + b + c

# Create a list of numbers
numbers = [3, 5, 7]

# Call the function using unpacking

print(add_three(*numbers))


# 14. Create a function describe_person(name, age, city)

# Create a dictionary:
person = {
    "name": "Ana",
    "age": 28,
    "city": "Porto"
}

# Call the function using unpacking

def describe_person(name, age, city):
    print(f"Name: {name}, \nAge: {age}, \nCity: {city}")

describe_person(**person)


# ------------------
# Real World Thinking
# ------------------

# 15. Create a function calculate_average(*numbers)
# Return the average of the numbers

def calculate_average(*numbers):
    count_num = 0
    total_sum = 0

    for num in numbers:
        count_num += 1
        total_sum += num
    
    return total_sum / count_num

print(calculate_average(2, 4, 6))

# 16. Create a function print_settings(**setings)
# Print each setting like:
# setting_name -> value

def print_settings(**settings):
    for key, value in settings.items():
        print(f"{key} -> {value}")

print_settings(name = "Ana", age = 26)

# 17. Create a function store_data(*args, **kwargs)

# Print:
# "Data: "
# Print positional values
# Print keyword values

def store_data(*args, **kwargs):
    print("Data: ")

    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(value)


# ------------------
# Filtering Values
# ------------------

# 18. Create a function sum_even_numbers(*numbers)
# Return the sum of only even numbers

def sum_even_numbers(*numbers):
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += num
    
    return total

print(sum_even_numbers(1, 2, 3, 4))


# 19. Create a function print_long_word(*words)
# Print only words longer than 5 characters

def print_long_word(*words):
    for word in words:
        if len(word) > 5:
            print(word)


print_long_word("chair", "elephant", "zebras", "dog")


# ------------------
# Bonus Challenge
# ------------------

# 20. Create a function create_user(**data)
# Required fields:
# name
# email

# If both exist:
# print "User created"
# Otherwise:
# print "Missing required information"

def create_user(**data):
    if "name" in data and "email" in data:
        print("User created")
    else:
        print("Missing required information")


create_user(name = "Joao", email = "joaopereira")