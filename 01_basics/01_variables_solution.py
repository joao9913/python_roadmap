# ------------------
# Numeric 
# ------------------

# 1. Create a two integer variables a and b. Print their sum, difference, product and division.
a = 10
b = 5
sum = a + b
diff = a - b
product = a * b
division = a / b
print("Sum: ", sum, "\nDifference", diff, "\nProduct", product, "\nDivision", division)

# 2. Create a complex number c = 4 + 5j. Print its real and imaginary parts.
c = 4 + 5j
print("\nReal: ", c.real, "\nImaginary", c.imag)

# ------------------
# String
# ------------------

# 1. Create a string variable greeting = "Hello" and another name = "Alice".
# Commbine them into one string "Hello, Alice" and print it.
greeting = "Hello"
name = "Alice"
phrase = greeting + ", " + name + "!"
print(phrase)

# 2. Print the length of greeting and convert it to uppercase
print(len(greeting))
print(greeting.upper())

# ------------------
# List / Tuple
# ------------------
# 1. Create a list of 5 numbers. Print the first element, last element, and a slice of the middle three elements
nums = [1, 2, 3, 4, 5]
print(nums[0])
print(nums[len(nums) - 1])
middle_three = nums[1:4]
print(middle_three)

# 2. Convert that list into a tuple and try to change the first element. Observe what happens.
tuple_nums = tuple(nums)
#tuple_nums[0] = 2

# ------------------
# Set
# ------------------
#1. Create a set with duplicate numbers: {1, 2, 2, 3, 3, 3}. Print it — what happens to duplicates?
nums_set = {1, 2, 2, 3, 3, 3}
print(nums_set)

#2. Add a new element to the set, then remove one element. Print the final set.
nums_set.add(10)
print(nums_set)

nums_set.remove(2)
print(nums_set)

# ------------------
# Dictionary
# ------------------
#1. Create a dictionary for a client with keys: "name", "age", "balance".
# Print the client’s name.
# Update the balance by adding 100.
# Add a new key "status" with value "active".
dictionary = {
    "name": "name", 
    "age": 1,
    "balance": 10
}
print(dictionary["name"])
dictionary["balance"] += 100
print(dictionary["balance"])
dictionary["status"] = "active"
print(dictionary)

# ------------------
# Boolean
# ------------------
# 1. Create two variables: x = 10, y = 20.
#Print the result of x > y and x < y.
#Combine two comparisons using and and or.
x = 10
y = 20
print(x > y)
print(x < y)
print(x < y and x > y)
print(x < y or x > y)

# ------------------
# NoneType / Mixed
# ------------------
#1. Create a variable z = None. Check if it is None using is.
z = None
if z is None:
    print("Z is none")

#2. Create a new variable that stores a list of mixed types: [int_number, string_example, boolean_example]. 
# Print each element’s type.
mixed_list = [2, "hello", True]
for item in mixed_list:
    print(type(item))