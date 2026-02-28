# ------------------
# Numeric 
# ------------------

# 1. Create two integers where:
# / returns a float
# // returns a different result

int_a = 5
int_b = 2
print("Division: ", int_a / int_b)
print("Floor Division: ", int_a // int_b)
# These differ because division = 2.5 float and floor division = 2 (floor toward negative infinity)

# 2. Create: a = "10"; b = 5
# Make the addition work without changing the value of a
# Then, make it work without changing the value of b

a = "10"
b = 5
addition = a + str(b)
print("Addition: ", addition)
addition = int(a) + b
print("Addition: ", addition)


print("\n")
# ------------------
# String
# ------------------

# 1. Create a string: s = "python". 
# Attempt to change the first character to uppercase using indexing.
# Observe the error
# Then, correctly produce "Python"

s = "python"
#s[0] = "S" # does not support item assignemnt
print("Upper: ", s.capitalize())

# 2. Without using loops, reverse: text = "DataTypes"
text = "DataTypes"
reversed_text = text[: : -1]    # start to end, step = -1 (Reverse direction)
print(reversed_text)


print("\n")
# ------------------
# Lists
# ------------------

# 1. Append 99 to copy1
# Append 100 to copy 2
# Print all three lists and explain what happened
original = [1, 2, 3]
copy1 = original
copy2 = original.copy()

print(f"original: {original}\ncopy1: {copy1}\ncopy2: {copy2}\n")
copy1.append(99)
print(f"original: {original}\ncopy1: {copy1}\ncopy2: {copy2}\n")
copy2.append(100)
print(f"original: {original}\ncopy1: {copy1}\ncopy2: {copy2}\n")

#append(99) altered the original list because they both share the same memory address
#append(100) only altered copy2 because we used .copy() to create a new copy of the original list

#2. 
nested = [[1, 2], [3, 4]]
copy_nested = nested.copy()

# Modify an inner list:
copy_nested[0].append(99)

print(f"nested: {nested}\ncopy: {copy_nested}")
#Both changed because im appending to the inner list. Copy contains the original nested lists, not copies.


print("\n")
# ------------------
# Tuples
# ------------------

#1. Create t = (1, [2, 3], 4)
# Modify the list inside the tuple
# Explain why this works even though tuples are immutable

t = (1, [2, 3], 4)
t[1].append(5)
print(t)
#This works because the list is still mutable, even though its inside an immutable tuple


print("\n")
# ------------------
# Sets
# ------------------

# 1. Given nums = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates using a set
# Convert back to a list
# What property of sets make this work?

nums = [1, 2, 2, 3, 4, 4, 5]
set_nums = set(nums)
print(f"list: {nums}\nset: {set_nums}")
new_list = list(set_nums)
print(new_list)
# Sets are unique, so duplicate elements are removed

# 2. Create two sets of numbers. Print: Union, Intersection, Elements only in first set. Explain each result
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
print("Union: ", set_1 | set_2) # All unique elements from both sets
print("Intersection: ", set_1 & set_2) # Elements that exist in both sets 
print("Elements only in set 1: ", set_1 - set_2) # Elements from set1 that dont exist in set 2


print("\n")
# ------------------
# Dictionary
# ------------------

# 1. Create a dictionary: user = {"name": "Joao", "age": 26}
# Try to access a key "balance" safely without raising an error
user = {
    "name": "Joao",
    "age": 26
}

print(user.get("balance"))  # .get() returns None if key doesn't exist

# 2. Iterate through the dictionary and 
# Print only keys
# Print only values
# Print both formatted with f-strings

for key, value in user.items():
    print(key)
    print(value)
    print(f"key: {key}\nvalue: {value}")


print("\n")
# ------------------
# Booleans & Truthiness
# ------------------

# 1. Test the boolean value of:
# 0, 1, "", "text", [], [0], None
# Explain the pattern

print(bool(0))  # False
print(bool(1))  # True
print(bool("")) # False
print(bool("text")) # True
print(bool([]))   # False
print(bool([0]))  # True
print(bool(None))   # False

# True and false alternate 


print("\n")
# ------------------
# Advanced Concepts
# ------------------

# 1. Check a == b; a is b
# Explain the difference
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# a == b actually compares one list to another, so its true
# a is b compares if the list actually is another one, so its false