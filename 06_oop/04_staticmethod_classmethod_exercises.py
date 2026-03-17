# ------------------
# Static Utility
# ------------------

# 1. Create a class called NumberUtils.
#
# Add a static method called is_even(number)
# that returns True if the number is even and False otherwise.
#
# Call the method using the class.



# ------------------
# Static Calculation
# ------------------

# 2. Create a class called GeometryUtils.
#
# Add a static method called circle_area(radius)
# that returns the area of a circle.
#
# Do not store any object state.



# ------------------
# Static Validation
# ------------------

# 3. Create a class called EmailValidator.
#
# Add a static method called is_valid(email)
# that returns True if the email contains "@" and ".".
#
# This method should not rely on instance or class data.



# ------------------
# Class Method Reading Class Data
# ------------------

# 4. Create a class called AppConfig.
#
# Add a class variable:
# - version = "1.0"
#
# Add a class method get_version()
# that returns the current version.



# ------------------
# Class Counter
# ------------------

# 5. Create a class called Session.
#
# Add a class variable called active_sessions.
#
# Each time a new Session object is created,
# increase the counter.
#
# Add a class method get_active_sessions()
# that returns the total.



# ------------------
# Factory Class Method
# ------------------

# 6. Create a class called User.
#
# Instance attributes:
# - username
#
# Create a class method called guest_user()
# that returns a User object with username = "Guest".



# ------------------
# Alternative Constructor
# ------------------

# 7. Create a class called Temperature.
#
# Instance attribute:
# - celsius
#
# Add a class method from_fahrenheit(f)
# that converts Fahrenheit to Celsius and
# returns a Temperature object.



# ------------------
# Static Helper Inside a Class
# ------------------

# 8. Create a class called PasswordUtils.
#
# Add a static method called is_strong(password)
# that returns True if:
# - length >= 8
# - contains at least one number
#
# No instance or class variables should be used.



# ------------------
# Instance + Class Interaction
# ------------------

# 9. Create a class called Product.
#
# Instance attributes:
# - name
# - price
#
# Class variable:
# - tax_rate = 0.2
#
# Add:
# - an instance method final_price() that includes tax
# - a class method set_tax_rate(new_rate)



# ------------------
# Class Method as Object Builder
# ------------------

# 10. Create a class called Coordinate.
#
# Instance attributes:
# - x
# - y
#
# Add a class method from_tuple(data)
# where data is a tuple like (x, y).
#
# The method should return a Coordinate object.



# ------------------
# Static Method for Comparison
# ------------------

# 11. Create a class called ScoreUtils.
#
# Add a static method higher_score(a, b)
# that returns the larger value.



# ------------------
# Static Method for Data Transformation
# ------------------

# 12. Create a class called TextFormatter.
#
# Add a static method normalize(text)
# that:
# - removes leading/trailing spaces
# - converts the text to lowercase.



# ------------------
# Class-Level Limits
# ------------------

# 13. Create a class called ApiClient.
#
# Class variable:
# - request_limit = 100
#
# Add a class method set_limit(new_limit)
# to update the limit.
#
# Add another class method get_limit().



# ------------------
# Class Method Tracking Instances
# ------------------

# 14. Create a class called Worker.
#
# Class variable:
# - worker_count
#
# Increase it every time a Worker object is created.
#
# Add a class method total_workers().



# ------------------
# Static Method for Input Checking
# ------------------

# 15. Create a class called AgeChecker.
#
# Add a static method is_adult(age)
# that returns True if age >= 18.



# ------------------
# Factory with Multiple Parameters
# ------------------

# 16. Create a class called Rectangle.
#
# Instance attributes:
# - width
# - height
#
# Add a class method square(size)
# that creates a rectangle where width and height are equal.



# ------------------
# Concept Review
# ------------------

# 17. In comments, explain:
#
# - When should you use a static method?
# - When should you use a class method?
# - What does "cls" represent?
# - Why are class methods often used as factory methods?
# - Why shouldn't static methods depend on instance data?
