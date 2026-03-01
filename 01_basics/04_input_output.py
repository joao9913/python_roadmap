"""
input_output.py
Topic: Input & Output
Goal: Understand user input, printing, formatting, file handling, and data conversion
"""

# ------------------
# Basic Output
# ------------------

print("Hello, World")

# print() sends output to the standard output stream (stdout).
# By default, it adds a new line at the end.


# ------------------
# Print Parameters
# ------------------

print("Python", "is", "powerful")           # Default separator: space
print("Python", "is", "powerful", sep="-")  # Custom separator
print("Hello", end=" ")                     # Custom end character
print("World")

# sep= defines how values are separated.
# end= defines what is printed at the end.


# ------------------
# Basic Input
# ------------------

name = input("Enter your name: ")

# input() always returns a string
# Even if the user types a number


# ------------------
# Type Conversion
# ------------------

age_input = input("Enter your age: ")
age = int(age_input)    # Explicit conversion required

# Common conversions:
# int()
# float()
# bool()    (rarely used directly on input)
# str()


# ------------------
# Input Validation (Basic Concept)
# ------------------

number_str = input("Enter a number: ")

if number_str.isdigit():
    number = int(number_str)
else:
    print("Invalid input")

# isdigit() checks if all characters are numeric.


# ------------------
# Formatted Output
# ------------------

user = "Joao"
score = 95

print(f"{user} scored {score}%")
print("{} scored {}%".format(user, score))
print(user + "scored" + str(score) + "%")

# f-strings are preferred for readibility and performance.


# ------------------
# Multi-line Output
# ------------------

multi_line = """
Line 1
Line 2
Line 3
"""

print(multi_line)

# Triple quotes allow multi-line strings.


# ------------------
# Reading Files
# ------------------

# Basic file reading pattern

file = open("example.txt", "r")
content = file.read()
file.close()

# Modes:
# r - read
# w - write (overwrite)
# a - append
# rb - read binary


# ------------------
# Recommended File Handling (with statement)
# ------------------

with open("example.txt", "r") as file:
    content = file.read()

# with automatically closes the file
# this prevents resource leaks


# ------------------
# Writing to Files
# ------------------

with open("output.txt", "w") as file:
    file.write("Hello\n")
    file.write("World\n")

# "w" overwrites file if it exists
# use "a" to append


# ------------------
# Reading Line by Line
# ------------------

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Iterating over a file reads one line at a time
# More memory-efficient that read() for large files


# ------------------
# Exception Handling (Basic I/O Errors)
# ------------------

try:
    with open("missing.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found")

# File I/O often requires error handling


# ------------------
# Standard Streams Concept
# ------------------

# sys.stdin - input stream
# sys.stdou - output stream
# sys.stderr - error stream

# print() writes to stdout by default



# ------------------
# Encoding Awareness
# ------------------

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Always specify encoding in real applications.
# Prevents platform-specific bugs