# ------------------
# Basic Property (Read)
# ------------------

# 1. Create a class called User.
#
# Instance attribute:
# - _username
#
# Add a property username that returns the value.


# ------------------
# Property with Validation (Write)
# ------------------

# 2. Create a class called Product.
#
# Instance attribute:
# - _price
#
# Add:
# - a property price
# - a setter that only allows values >= 0


# ------------------
# Prevent Invalid State
# ------------------

# 3. Create a class called BankAccount.
#
# Instance attribute:
# - _balance
#
# Add:
# - a property balance
# - a setter that prevents negative values


# ------------------
# Read-Only Property
# ------------------

# 4. Create a class called Circle.
#
# Instance attribute:
# - _radius
#
# Add a read-only property area that calculates:
# π * radius^2
#
# Do NOT allow setting area.


# ------------------
# Property Depending on Multiple Attributes
# ------------------

# 5. Create a class called Rectangle.
#
# Instance attributes:
# - _width
# - _height
#
# Add a property area that returns width * height.


# ------------------
# Validation with Multiple Conditions
# ------------------

# 6. Create a class called Person.
#
# Instance attribute:
# - _age
#
# Add:
# - a property age
# - a setter that only allows:
#     age >= 0
#     age <= 120


# ------------------
# Derived Property
# ------------------

# 7. Create a class called Employee.
#
# Instance attributes:
# - _salary
#
# Add:
# - a property yearly_salary (salary * 12)
# - no setter for yearly_salary


# ------------------
# Controlled Update
# ------------------

# 8. Create a class called Temperature.
#
# Instance attribute:
# - _celsius
#
# Add:
# - a property celsius
# - a setter that prevents values below -273.15


# ------------------
# Multiple Properties
# ------------------

# 9. Create a class called Box.
#
# Instance attributes:
# - _width
# - _height
#
# Add:
# - property width (with validation > 0)
# - property height (with validation > 0)
# - property area (read-only)


# ------------------
# Property with Transformation
# ------------------

# 10. Create a class called Text.
#
# Instance attribute:
# - _content
#
# Add:
# - a property content (returns original)
# - a property normalized (returns lowercase + stripped text)


# ------------------
# Write-Only Behavior Simulation
# ------------------

# 11. Create a class called Password.
#
# Instance attribute:
# - _password
#
# Add:
# - a setter for password that:
#     - requires length >= 8
# - a getter that raises an exception or prevents reading


# ------------------
# Property Triggering Logic
# ------------------

# 12. Create a class called LightSwitch.
#
# Instance attribute:
# - _is_on (boolean)
#
# Add:
# - a property is_on
# - a setter that only accepts True/False


# ------------------
# Encapsulation with Internal Method Use
# ------------------

# 13. Create a class called Score.
#
# Instance attribute:
# - _value
#
# Add:
# - a property value
# - a setter that prevents values < 0
# - a method add(points) that updates value safely


# ------------------
# Property + Class Interaction
# ------------------

# 14. Create a class called ApiClient.
#
# Instance attribute:
# - _requests_made
#
# Class variable:
# - max_requests = 100
#
# Add:
# - property requests_made
# - setter that prevents exceeding max_requests


# ------------------
# Dependent Property Update
# ------------------

# 15. Create a class called Rectangle.
#
# Instance attributes:
# - _width
# - _height
#
# Add:
# - property width (with validation)
# - property height (with validation)
# - property perimeter = 2 * (width + height)


# ------------------
# Data Integrity (Multiple Constraints)
# ------------------

# 16. Create a class called Account.
#
# Instance attributes:
# - _username
# - _balance
#
# Add:
# - username property (non-empty string)
# - balance property (>= 0)


# ------------------
# Property with Conditional Logic
# ------------------

# 17. Create a class called Student.
#
# Instance attribute:
# - _grade
#
# Add:
# - property grade
# - setter that only allows values between 0 and 100


# ------------------
# Concept Review
# ------------------

# 18. In comments, explain:
#
# - Why use _protected attributes instead of public ones?
# - What problem does @property solve?
# - When should you NOT use a setter?
# - What is a read-only property?
# - How do properties improve API design?
