"""
04_input_output_exercises.py
Topic: Input & Output
Goal: Practice user input, type conversion, validation, formatting, file reading/writing, and error handling
"""

# ------------------
# Basic Output
# ------------------

#1. Print the following exactly:
# Name: Joao
# Age: 26
# Country: Portugal

# a) Using multiple print() statements
print("Name: Joao")
print("Age: 26")
print("Country: Portugal")

# b) Using a single multi-line string
multiline = """
Name: Joao
Age: 26
Country: Portugal
"""
print(multiline)


# ------------------
# Print Parameters
# ------------------

# 2. Print the numbers 1 to 5 on the same line separated by " | "
print(*range(1, 6), sep=" | ")


# ------------------
# Basic Input & Type Conversion
# ------------------

# 3. Ask the user for:
# Their name
# Their birth year

name = input("Name: ")
birth_year = input("Birth Year: ")

# a) Convert the birth year to an integer
year = int(birth_year)

# b) Calculate their approximate age (assume current year is 2025)
age = 2025 - year

# c) Print: "Hello <name>, you are approximately <age> years old."
print(f"Hello {name}, you are approximately {age} years old.")


# ------------------
# Input Validation
# ------------------

# 4. Ask the user to enter a number.
number = input("Enter a number: ")

# a) If the input is numeric, convert it to int and print its square
if number.isdigit():
    square = int(number) ** 2
    print(f"Square: {square}")

# b) If not numeric, print "Invalid number"
else:
    print("Invalid number")


# ------------------
# Advanced Input Validation
# ------------------

# 5. Ask the user to enter a floating-point number.
float_num = input("Enter a floating-point number: ")

# Use try/except to:
# a) Attempt conversion using float()
# b) If conversion fails, print "Invalid input"
# c) If successful, print half of the number

try:
    num = float(float_num)
    print(str(num / 2))
except ValueError:
    print("Invalid input")


# ------------------
# String Formatting Practice
# ------------------

# 6. Ask the user for:
# - Product name
# - Product price (float)

product = input("Product name: ")
price = input("Price: ")

# a) Format the price to 2 decimal places.
price_float = round(float(price),2 )

# b) Print: "<product> costs $<price>"
print(f"{product} costs ${price_float}")


# ------------------
# Writing To a File
# ------------------

# 7. Create a file called "user_info.txt"
# Ask the user for: name and age
# Write this to the file:
# Name <name>
# Age: <age>
# Use a with statement

with open("user_info.txt", "w") as file:
    user_name = input("Name: ")
    user_age = input("Age: ")
    file.write(f"Name: {user_name}\n")
    file.write(f"Age: {user_age}\n")


# ------------------
# Appending to a File
# ------------------

# 8. Append a new line to "user_info.txt":
# "Status: Active"

with open("user_info.txt", "a") as file:
    file.write("Status: Active\n")


# ------------------
# Reading From a File
# ------------------

# 9. Read the contents of "user_info.txt"

with open("user_info.txt", "r") as file:
    # a) Print the entire content
    content = file.read()
    print(content)


# ------------------
# File Existence Handling
# ------------------

# 10. Attempt to open a file named "missing_file.txt"
# Use try/except
# Catch "FileNotFoundError"
# Print "File does not exist"

try:
    with open("missing_file.txt", "r") as file:
        print()
except FileNotFoundError:
    print("File does not exist")


# ------------------
# Working With Numbers From a File
# ------------------

# 11. Create a file named "numbers.txt"
# Write the numbers 1 through 5 into it (one per line)
# Then:
# a) Read the file
# b) Convert each line to an integer
# c) Calculate the total sum
# D) Print the sum


with open("numbers.txt", "w") as file:
    for num in range(1,6):
        file.write(str(num) + "\n")  

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        num = int(line)
        total += num
    
    print(total)


# ------------------
# Bonus: Simple Logger
# ------------------

# 12. Create a small logging system.
# Ask the user to enter a message.
message = input("Enter a message")

with open("log.txt", "a") as file:
    file.write(f"\n--- New Entry ---\nMessage: {message}\n")