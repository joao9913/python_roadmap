# ------------------
# Basic Iteration
# ------------------

# 1. Given:
numbers = [3, 7, 2, 9, 12]

# Print each number in the list
for num in numbers:
    print(num)


# ------------------
# Accumulator Pattern
# ------------------

# 2. Given
numbers = [5, 10, 15, 20]

# Calculate and print the total sum of numbers

total = 0
for num in numbers:
    total += num

print(total)


# ------------------
# Counting Pattern
# ------------------

# 3. Given:
numbers = [1, 4, 6, 8, 3, 10]

# Count how many numbers are even
# Print the final count

num_evens = 0

for num in numbers:
    if num % 2 == 0:
        num_evens += 1

print(num_evens)


# ------------------
# Filtering
# ------------------

# 4. Given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Print only numbers greater than 4.

for num in numbers:
    if num > 4:
        print(num)


# ------------------
# range()
# ------------------

# 5. Print numbers from 1 to 10 (inclusive) using range()

for i in range(1, 11):
    print(i)


# ------------------
# range() with step
# ------------------

#6. Print all odd numbers between 1 and 20 using range()

for i in range(1, 21, 2):
    print(i)


# ------------------
# Iterating over strings
# ------------------

# 7. Given:
text = "Programming"

# Count how many vowels are in the string
# (vowels: a, e, i, o, u - lowercase only)

vowels = ["a", "e", "i", "o", "u"]
total = 0

for char in text:
    for i in vowels:
        if char == i:
            total += 1
            break

print(total)


# ------------------
# enumerate()
# ------------------

# 8. Given:
fruits = ["apple", "banana", "cherry"]

# Print:
# 0 - apple
# 1 - banana
# 2 - cherry
# use enumerate()

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ------------------
# break
# ------------------

# 9. Given
numbers = [2, 4, 6, 8, 11, 14]

# Loop through the list
# Stop the loop when you find the first odd number
# Print the number

for num in numbers:
    if num % 2 != 0:
        print(num)
        break


# ------------------
# continue
# ------------------

# 10. Given:
numbers = [1, 2, 3, 4, 5, 6]

# Print only even numbers
# Use continue explicitly

for num in numbers:
    if num % 2 != 0:
        continue

    print(num)


# ------------------
# for - else
# ------------------

# 11. Given:
numbers = [2, 4, 6, 8]

# Check if there is any odd number in the list
# If an odd number is found, print "Odd found"
# If the loop completes without finding one, print "All numbers are even"
# Use for-else

for num in numbers:
    if num % 2 != 0:
        print("Odd found")
        break
else:
    print("All numbers are even")


# ------------------
# Nested Loops
# ------------------

# 12. Print the following pattern:
#
# *
# ** 
# ***
# ****

# Use nested loop

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()


# ------------------
# Dictionary Iteration
# ------------------

# 13. Given:
person = {
    "name": "Joao",
    "age": 26,
    "country": "Portugal"
}

# Print each key and its corresponding value

for key, value in person.items():
    print(key, value)


# ------------------
# zip ()
# ------------------

# 14. Given:
names = ["Ana", "Bruno", "Carlos"]
scores = [85, 90, 78]

# Print:
# Ana scored 85
# Bruno scored 90
# Carlos scores 78

for name, scores in zip(names, scores):
    print(f"{name} scored {scores}")


# ------------------
# Maximum Value (Manual)
# ------------------

# 15. Given:
numbers = [4, 17, 2, 9, 21, 6]

# Find the maximum number WITHOUT using max()
# Use a loop

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    
print(max_num)


# ------------------
# Multiplication Table
# ------------------

# 16. Print the multiplication table of 5:

# 5 x 1 = 5
# 5 * 2 = 10
# ...
# use range()

for i in range(1, 11):
    print(f"5 x {i} = ", 5*i)


# ------------------
# Reverse Iteration
# ------------------

# 17. Print numbers from 10 down to 1 using range()

for i in range(10, 0, -1):
    print(i)


# ------------------
# Early Exit Optimization
# ------------------

# 18. Given:
numbers = [1, 3, 5, 7, 3, 9]

# Determine if the list contains any even number
# Stop the loop as soon as one is found
# Print True or False

for num in numbers:
    if num % 2 == 0:
        print("True")
        break
else:
    print("False")