# ------------------
# Local Scope
# ------------------

# 1. Create a function show_number()
# Inside the function create a variable number = 10
# Print the variable inside the function
# Call the function

def show_number():
    number = 10
    print(number)

show_number()


# ------------------
# Local Variable Error
# ------------------

# 2. Create a function create_message()
# Inside the functin create a variable message = "Hello"
# Print the message inside the function
# Then try printing message outside the function
# Observe what happens 

def create_message():
    message = "Hello"
    print(message)

# print(message)    # wont work because message is defined inside the function


# ------------------
# Global Variable Access
# ------------------

# 3. Create a global variable:
# price = 50
# Create a function show_price()
# Print the price inside the function
# Call the function

price = 50

def show_price():
    print(price)

show_price()


# ------------------
# Local vs Global Variable
# ------------------

# 4. Create a global variable:
# value = 100

# Create a function test_value()
# Inside the function create a local variable value = 20
# Print value inside the function

# Then print value outside the function
# Observe the difference

value = 100

def test_value():
    value = 20
    print(value)

test_value()
print(value)


# ------------------
# Modifying Global Variable
# ------------------

# 5. Create a global variable:
# counter = 0

# Create a function increase_counter()
# Use the global keyword
# Increase counter by 1

# Call the function 3 times
# Print counter

counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()
increase_counter()
print(counter)


# ------------------
# Global Variable Read Only
# ------------------

# 6. Create a global variable:
# tax = 0.23

# Create a function calculate_total(price)
# Return price + price * tax

# Call the function with price = 100
# Print the result

tax = 0.23

def calculate_total(price):
    return price + price * tax

print(calculate_total(100))


# ------------------
# Nested Functions
# ------------------

# 7. Create a function outer()

# Inside it create a variable message = "Hello from outer"

# Inside outer() create another function inner()
# Print message inside inner()

# Call inner() inside outer()
# Then call outer()

def outer():
    message = "Hello from outer"

    def inner():
        print(message)
    
    inner()

outer()


# ------------------
# Using a Global Counter
# ------------------

# 9. Create a global variable:
attempts = 0

# Create a function login_attempt()
# Increase attempts by 1 using global

# Call the function 5 times
# Print the total attempts

def login_attempt():
    global attempts
    attempts += 1

for i in range(5):
    login_attempt()

print(attempts)


# ------------------
# Multiple Functions Using Same Global
# ------------------

# 10. Create a global variable:
# balance = 1000

# Create two functions:
# deposit(amount)
# withdraw(amount)

# deposit should add money to balance
# withdraw should subtract money from balance

# Use the global keyword inside both functions

# Example calls:
# deposit(200)
# withdraw(150)

#Print the final balance

balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

deposit(200)
withdraw(100)
print(balance)


# ------------------
# Local Calculation Function
# ------------------

# 11. Create a function calculate_area(witdh, height)

# Inside the function create a variable area
# Store width * height

# Print the area inside the function

def calculate_area(width, height):
    area = width * height
    print(area)

calculate_area(2, 5)


# ------------------
# Scope Observation
# ------------------

# 12. Create a global variable:
x = 10

# Create a function test_scope()
# Inside the function:
# Create x = 5
# Print x

# After calling the function, print x again
# Observe which value is printed each time

def test_scope():
    x = 5
    print(x)

test_scope()
print(x)


# ------------------
# Bonus Challenge
# ------------------

# 13. Create a global variable
score = 0

# Create two functions:

# add_points(points)
# subtract_points(points)

# Both functions should modify score using global

# Example:
# add_points(10)
# subtract_points(3)

# Print the final score

def add_points(points):
    global score
    score += points

def subtract_points(points):
    global score
    score -= points

add_points(10)
subtract_points(3)
print(score)