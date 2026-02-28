"""
03_strings_.py
Topic: Strings
Goal: Understand string creation, indexing, slicing, methods and immutability
"""

# ------------------
# Creating Strings
# ------------------

single_quotes = 'Python'
double_quotes = "Python"
triple_quotes = """Python
is
multiline"""

#String are immutable sequences of unicode characters


# ------------------
# Indexing
# ------------------

text = "DataTypes"

first_character = text[0] #D
last_character = text[-1] #S

# Strings are zero-indexed
# Negative indexing counts from the end


# ------------------
# Slicing
# ------------------

full_text = text[:]
first_part = text[:4]   #Data
second_part = text[4:]  #Types
reversed_text = text[::-1]  #sepyTataD
every_second = text[::2]    #DtTps

# Slicing format: [start:stop:step]
# Start inclusive, stop exclusive
# Slicing returns a new string


# ------------------
# Immutability
# ------------------

word = "python"
#word[0] = "P"  #TypeError (strings do not support item assignment)

modified_word = word.capitalize() # creates a new string

#Any modification produces a new object


# ------------------
# String Methods
# ------------------

messy = "    PyTHon    "
lower_case = messy.lower()
upper_case = messy.upper()
capitalized = messy.capitalize()
title_case = messy.title()
stripped = messy.strip()
left_striped = messy.lstrip()
right_striped = messy.rstrip()
replaced = messy.replace("PyTHon", "Java")

# Methods return new strings


# ------------------
# Searching
# ------------------

sentence = "Python is powerful"

contains_python = "Python" in sentence  #True
position = sentence.find("is")  # Returns index
# sentence.index("Java") would raise ValueError


# ------------------
# Splitting & Joining
# ------------------

words = sentence.split()    # ["Python", "is", "powerful"]
dash_joined = "-".join(words)   # "Python-is-powerful"
pipe_joined = "|".join(words)   # "Python|is|powerful"

# join() belongs to the separator string


# ------------------
# String Formatting
# ------------------

name = "Joao"
age = 26

concatenation = name + "is" + str(age) + " years old"
formatted_old = "{} is {} years old".format(name, age)
formatted_f = f"{name} is {age} years old"

# f-strings are preferred (readable and efficient)


# ------------------
# Unicode & Encoding
# ------------------

word_unicode = "café"

length_characters = len(word_unicode)
length_bytes = len(word_unicode.encode("utf-8"))

# Character count and byte count may differ


# ------------------
# Identity vs Equality
# ------------------

a = "python"
b = "python"

value_comparison = (a == b) # True
identity_comparison = (a is b)  # May be True due to interning

# Always use == for string comparison