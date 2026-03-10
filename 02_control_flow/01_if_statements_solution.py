# ------------------
# Basic Conditions
# ------------------

# 1. Given:
age = 20

# a) Print "Adult" if age is 18 or older
if age >= 18:
    print("Adult")

# b) Otherwise print "Minor"
else:
    print("Minor")


# ------------------
# If / Else Logic
# ------------------

# 2. Given:
number = 7

# a) Print "Even" if the number is even

if number % 2 == 0:
    print("Even")

# b) Print "Odd" otherwise
else:
    print("Odd")


# ------------------
# If Elif Else
# ------------------

# 3. Given:
score = 82

# Print:
# "A" if score >= 90
# "B" if score >= 80
# "C" if score >= 70
# "D" otherwise

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# ------------------
# Logical Operators
# ------------------

# 4. Given:
temperature = 25
is_sunny = True

# Print "Go to the beach" if:
# temperature is greater than 20 AND it is sunny
# Otherwise print "Stay home"

if temperature > 20 and is_sunny:
    print("Go to the beach")
else:
    print("Stay home")


# ------------------
# OR Condition
# ------------------

# 5. Given:
day = "Saturday"

# Print "Weekend" if the day is Saturday OR Sunday
# Otherwise print "Weekday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# ------------------
# NOT Operator
# ------------------

# 6. Given:
is_logged_in = True

# Print "Access granted" if the user is logged in
# Otherwise print "Access denied"
# Use the NOT operator explicitly

if not is_logged_in:
    print("Access denied")
else:
    print("Access granted")


# ------------------
# Truthiness
# ------------------

# 7. Given
items = []

# a) Print "Cart is empty" if the list is empty
if not items:
    print("Cart is empty")
else:
    print("Cart has items")


# ------------------
# Membership Testing
# ------------------

# 8. Given:
username = "joao_admin"

# a) If "admin" is in the username, print "Admin user"
# b) Otherwise print "Regular user"

if "admin" in username:
    print("Admin user")
else:
    print("Regular user")


# ------------------
# Chained Comparisons
# ------------------

# 9. Given:
num = 19

# Print "Within range" if num is strictly between 10 and 20
# Use chained comparison (not two separate conditions).

if 10 < num < 20:
    print("Within range")


# ------------------
# Nested If Statements
# ------------------

# 10. Given:
age = 22
has_ticket = True

# If age is 18 or older:
#   If has_ticket is True:
#       Print "Entry allowed"
#   Otherwise:
#       Print "Ticket required"
# Otherwise:
#   Print "Underage"

if age >= 18:
    if has_ticket:
        print("Entry allowed")
    else:
        print("Ticket required")
else:
    print("Underage")


# ------------------
# Overlapping Condition Trap
# ------------------

# 1. Given: 
score = 95

# Write conditions so that:
# - "Excelent" prints for scores >= 90
# - "Pass" prints for scores >= 60
# - "Fail" prints otherwise
# Make sure "Excelent" is not skipped

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")


# ------------------
# Identity vs Equality
# ------------------

# 12. Given
value = None

# a) Check properly if value is None
# b) Print "Value missing" if it is None

if value is None:
    print("Value missing")


# ------------------
# Short-Circuit Evaluation
# ------------------

# 13. What will this print? Explain why

x = 0

if x != 0 and 10 / x > 1:
    print("Condition met")
else:
    print("Condition not met")

# Prints Condition not met, because x == 0 and x cant be 0 for the if to run


# ------------------
# Ternary Operator
# ------------------

# 14. Given:
age = 17

# Create a variable called status that stores:
# "Adult" if age >= 18
# "Minor" otherwise
# Use a one-line conditional expression

status = "Adult" if age >= 18 else "Minor"
print(status)