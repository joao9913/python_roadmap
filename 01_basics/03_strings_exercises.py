"""
03_strings_exercises.py
Topic: Strings
Goal: practice indexing, slicing, immutability, methods, formatting and string behaviour
"""

# ------------------
# Basic Indexing
# ------------------

# 1. Given:
text = "Programming"

# a) Print the first character
# b) Print the last character
# c) Print the third character
# d) Print the second-to-last character

print(text[0])
print(text[-1])
print(text[2])
print(text[-2])


# ------------------
# Slicing Practice
# ------------------

# 2. Using only slicing (no loops), produce:

word = "DataScience"

# a) "Data"
# b) "Science"
# c) Reverse the string
# d) Every second character
# e) "cneiSataD"

print(word[0:4])
print(word[4:])
print(word[::-1])
print(word[::2])
print(word[-2::-1])


# ------------------
# Immutability
# ------------------

# 3. Attempo to change the first letter of:
language = "python"

# a) Observe the error
# b) Correctly produce "Python" without modifying the original string

#language[0] = "P" does not work, string is immutable
print(language.capitalize())


# ------------------
# String Methods
# ------------------

# 4. Given:
messy = "   PyTHon iS FuN   "

# a) Remove surrounding whitescape
messy = messy.rstrip()
messy = messy.lstrip()

# b) Convert eveything to lowercase
messy = messy.lower()

# c) Convert everything to uppercase
messy = messy.upper()

# d) Convert to proper sentence case: "Python is fun"
messy = messy.capitalize()

# e) Replace "FuN" with powerful
messy = messy.replace("fun", "powerful")

print(messy)


# ------------------
# Searching & Membership
# ------------------

# 5. Given:
sentence = "Python is simple and powerful"

# a) Check if "simple" exists in the string
if "simple" in sentence:
    print(f"simple is in {sentence}")

# b) Find the index of "powerful"
position = sentence.find("powerful")
print(position)

# c) What happens if you try to find "Java" using:
#   - .find()
#   - .index()

result = sentence.find("Java")  # Returns -1 because "Java" is not in sentence
# result = sentence.index("Java")   # Returns ValueError because "Java" is not a substring of sentence


# ------------------
# Splitting & Joining
# ------------------

# 6. Given:
phrase = "Learn Python step by step"

# a) Convert the string into a list of words
words = phrase.split(" ")

# b) Join the words using "-"
new_phrase = "-".join(words)

# c) Join the words using "|"
new_phrase = "|".join(words)


# ------------------
# String Formatting
# ------------------

# 7. Given:
name = "Joao"
score = 95

# Produce the string: "Joao scored 95% on the exam"

# a) Using concatenation
new_str = name + " scored " + str(score) + "% on the exam"

# b) Using .format()
new_str = "{} scored {}% on the exam".format(name, score)

# c) Using f-strings
new_str = f"{name} scored {score}% on the exam"


# ------------------
# Unicode & Encoding
# ------------------

# 8. Given:
word = "café"

# a) Print the number of characters
print(len(word))

# b) Print the number of bytes in UTF-8 encoding
print(len(word.encode("utf-8")))

# c) Explain why they differ
# Because the number of bytes of each character might not be the same value as the number of characters


# ------------------
# Identity vs Equality
# ------------------

# 9. Create two identical strings with the same value.
str_1 = "Thanks for playing"
str_2 = "Thanks for playing"

# Check:
# a) ==
print(str_1 == str_2)

# b) is
print(str_1 is str_2)

# Explain the difference between value equality and identity
# Equality compares values of each string, identity checks if a variable is actually the same as another variable


# ------------------
# Advanced: String Behaviour
# ------------------

# 10. What will this print? Explain why.

def shout(text):
    text.upper()
    return text

print(shout("hello"))

#This will print "hello" because we are returning the same input. text.upper() does not change the original text var


# ------------------
# Performance Awareness
# ------------------

# 11. Why is this inefficient?

result = ""
#for i in range(1000):
#    result += "a"

# Because each += creates a new string. O(n^2) complexity

# Rewrite it using a more efficient approach
result = "a" * 1000
print(result)


# ------------------
# Bonus Challenge
# ------------------

# 12. Given:
text = "  Data Types in PYTHON   "

# Produce exactly:
# "data-types-in-python"

# Constraints:
# - Remove extra whitespace
# - Convert to lowercase
# - Replace spaces with "-"
# - Do it in a clean chain of methods (one expression)

print(text.strip().lower().replace(" ", "-"))