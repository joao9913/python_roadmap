# ------------------
# Basic While Loop
# ------------------

# 1. Print numbers from 0 to 4 using a while loop

number = 0 
while number < 5:
    print(number)
    number += 1


# ------------------
# Reverse Counting
# ------------------

# 2. Print numbers from 10 down to 1 using a while loop

number = 10
while number > 0:
    print(number)
    number -= 1


# ------------------
# Accumulator Pattern
# ------------------

# 3. Given:
numbers = [5, 10, 15, 20]

# Use a while loop to calculate the sum of the numbers

total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print(total)


# ------------------
# Counting Pattern
# ------------------

# 4. Given:
numbers = [1, 2, 3, 4, 5, 6]

# Count how many numbers are odd using a while loop

index = 0
count_odd = 0

while index < len(numbers):
    if numbers[index] % 2 != 0:
        count_odd += 1
    
    index += 1

print(count_odd)


# ------------------
# Searching with Early Exit
# ------------------

# 5. Given
numbers = [10, 25, 30, 45, 50]
target = 30

# Use a while loop to determine if target exists in the list
# Stop the loop immediately when found
# Print True or False

index = 0

while index < len(numbers):
    if numbers[index] == target:
        print("True")
        break

    index += 1
else:
    print("False")


# ------------------
# Infinite Loop With Break
# ------------------

# 6. Create a while True loop that:
# - Prints numbers starting from 1
# - Stops when the number reaches 5
# Use break

num = 1

while True:
    print(num)
    if num == 5:
        break

    num += 1


# ------------------
# Continue Usage
# ------------------

# 7. Print numbers from 1 to 10
# Skip printing number 5
# Use continue explicitly

number = 0

while number < 10:
    number += 1
    if number == 5:
        continue

    print(number)


# ------------------
# Sentinel Value Loop
# ------------------

# 8. Keep asking the user to input a word
# Stop when the user types "stop"
# Print each word entered (except "stop")

while True:
    user_input = input("Input a word: ")

    if user_input == "stop":
        break

    print(user_input)


# ------------------
# Input Validation
# ------------------

# 9. Ask the user to enter a number greater than 0
# Keep asking until a valid number is entered
# Then print "Valid number"

number = 0

while number <= 0:
    number = int(input("Enter a number greater than 0: "))

print("Valid Number")


# ------------------
# Manual Maximum Search
# ------------------

# 10. Given:
numbers = [4, 17, 2, 9, 11, 6]

# Find the maximum number using a while loop
# Do NOT use max()

index = 0
max_num = numbers[index]

while index < len(numbers):
    max_num = numbers[index] if numbers[index] > max_num else max_num
    index += 1

print(max_num)


# ------------------
# Multiplication Table
# ------------------

# 11. Print the multiplication table of 7:
# 7 x 1 = 7
# ...
# 7 x 10 = 70

# Use a while loop

index = 1

while index < 11:
    print(f"7 x {index} = ", 7*index)
    index += 1


# ------------------
# While-else Behaviour
# ------------------

# 12. Given:
numbers = [2, 4, 6, 8]

# Check if any number is odd
# If found, print "Odd found"
# If loop completes normally, print "All even"
# Use while-else

index = 0
while index < len(numbers):
    if numbers[index] % 2 != 0:
        print("Odd found")
        break
    index += 1
else:
    print("All even")


# ------------------
# Index Tracking
# ------------------

# 13. Given:
text = "Python"

# Print each character using a while loop and index

index = 0
while index < len(text):
    print(text[index])
    index += 1


# ------------------
# Accumulate User Input
# ------------------

# 14. Keep asking the user to enter numbers
# Stop when the user enters 0
# Print the total sum of all entered numbers (excluding 0)

total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    total += number

print(total)


# ------------------
# Menu Loop
# ------------------

# 15. Create a simple menu loop:
# Print:
# 1 - Hello
# 2 - Bye
# exit - Quit
# - Execute the corresponding action
# - Keep looping until user types "exit"

option = ""

while option != "exit":
    option = input("Choose an option: ")

    if option == "1":
        print("Hello")
    elif option == "2":
        print("Bye")
    elif option == "exit":
        print("Quit")
    else:
        print("Invalid option")