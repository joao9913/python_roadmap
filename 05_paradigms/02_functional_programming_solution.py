from functools import reduce


# ------------------
# Lambda Functions
# ------------------

# 1. Create a lambda function that takes a number and returns True if it is positive.
# Test it with several values.

print("#1")

positive = lambda x: x > 0
print(positive(5))


# 2. Create a lambda function that returns the length of a string.
# Test it on a list of words using map().

print("\n#2")

words = ["developer", "python", "code", "functional"]
lenght_str = list(map(lambda x: len(x), words))
print(lenght_str)


# ------------------
# map()
# ------------------

# 3. Given a list of prices, use map() to add a 20% tax to each price.
# Return the new list.

print("\n#3")

prices = [10, 25, 40, 100]
price_taxed = list(map(lambda x: x * 1.2, prices))
print(price_taxed)


# 4. Given a list of usernames, use map() to convert them into dictionaries
# with the structure:
# {"username": "<name>"}

print("\n#4")

usernames = ["alice", "bob", "charlie"]
usernames_dict = list(map(lambda x: {"username": x}, usernames))
print(usernames_dict)


# ------------------
# filter()
# ------------------

# 5. Given a list of file names, use filter() to keep only files that end with ".py".

print("\n#5")

files = ["app.py", "config.json", "database.py", "notes.txt"]
files_py = list(filter(lambda x: x.endswith(".py"), files))
print(files_py)


# 6. Given a list of users represented as dictionaries,
# filter users who are active.

print("\n#6")

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
]

users_state = list(filter(lambda x: x["active"], users))

print(users_state)


# ------------------
# reduce()
# ------------------

# 7. Given a list of numbers, use reduce() to calculate the total sum.

print("\n#7")

numbers = [5, 10, 15, 20]

total_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Total sum: {total_numbers}")


# 8. Given a list of strings, use reduce() to join them into one sentence
# separated by spaces.

print("\n#8")

words = ["Functional", "programming", "is", "powerful"]

sentence_joined = reduce(lambda x, y: x + " " + y, words)
print(sentence_joined)


# ------------------
# Higher-Order Functions
# ------------------

# 9. Write a function apply_operation(func, value)
# that applies the given function to the value and returns the result.
# Test it with at least two different functions.

print("\n#9")

def apply_operations(func, value):
    return func(value)

squared = lambda x: x ** 2
cubed = lambda x: x ** 3

print(apply_operations(squared, 2))
print(apply_operations(cubed, 3))


# 10. Write a function transform_list(data, func)
# that applies a function to every element of the list using map()
# and returns the result.

print("\n#10")

data = [1, 2, 3, 4]

def transform_list(data, func):
    return list(map(func, data))

print(transform_list(data, squared))


# ------------------
# Function Composition
# ------------------

# 11. Write a function compose(f, g)
# that returns a new function equivalent to f(g(x)).

print("\n#11")

def compose(f, g):
    return lambda x: f(g(x))

f = lambda x: x ** 2
g = lambda x: x * 9
h = compose(f, g)

print(h(5))


# 12. Create two functions:
# - strip_spaces(text)
# - make_lower(text)
#
# Use your compose() function to combine them so that the final function
# cleans a string by stripping spaces and converting it to lowercase.

print("\n#12")

def strip_spaces(text):
    return list(filter(lambda x: x != " ", text))

def make_lower(text):
    return "".join(list(map(lambda x: x.lower(), text)))

cleaner = compose(make_lower, strip_spaces)
text_sample = "a  nT"
print(cleaner(text_sample))


# ------------------
# Data Transformation (Realistic Tasks)
# ------------------

# 13. Given a list of product dictionaries, use functional tools
# to create a list of only the product names.

print("\n#13")

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
]

def get_names(products):
    return list(map(lambda x: x["name"], products))

print(get_names(products))


# 14. Using filter(), create a list of products that cost more than 100.

print("\n#14")

def products_100(products):
    return list(filter(lambda x: x["price"] > 100, products))

print(products_100(products))


# 15. Using map(), create a list with the prices of all products
# after applying a 10% discount.

print("\n#15")

def discounted(products):
    return list(map(lambda x: x["price"] * 0.9, products))

print(discounted(products))


# ------------------
# Functional Pipelines
# ------------------

# 16. Starting from the list below:
# - Convert all numbers to their absolute value
# - Keep only numbers greater than 10
# - Square the remaining numbers
#
# Use a pipeline with map() and filter().

print("\n#16")

numbers = [-20, -5, 3, 12, 15, -30]

def pipeline(numbers):
    return list(map(lambda x: x ** 2,
                    filter(lambda x: x > 10,
                           map(lambda x: abs(x), numbers))))


print(pipeline(numbers))


# 17. From a list of sentences, produce a list containing
# the length of each sentence.

print("\n#17")

sentences = [
    "Functional programming is powerful",
    "Python supports multiple paradigms",
    "Write clean code",
]

length_sentences = list(map(lambda x: len(x), sentences))

print(length_sentences)


# ------------------
# Immutability Practice
# ------------------

# 18. Given a list of dictionaries representing users:
# Create a NEW list where each user has a new field:
# "role": "user"
#
# Do not modify the original list.

print("\n#18")

users = [
    {"name": "Alice"},
    {"name": "Bob"},
]

def add_role(element):
    new_element = {**element, "role": "user"}
    return new_element

new_users = list(map(add_role, users))

print(users)
print(new_users)


# ------------------
# Harder Challenges (Interview Style)
# ------------------

# 19. Given a list of log entries:
# Count how many times each log level appears.
#
# Example output:
# {"INFO": 2, "ERROR": 1, "WARNING": 1}
#
# Use reduce().

print("\n#19")

logs = ["INFO", "ERROR", "INFO", "WARNING"]

def reducer(acc, level):
    if level in acc:
        current_num = acc[level]
        new_acc = {**acc, level: current_num + 1}
        return new_acc

    new_acc = {**acc, level: 1}
    return new_acc

logs_count = reduce(reducer, logs, {})

print(logs_count)


# 20. Build a functional pipeline that:
# - Takes a list of numbers
# - Removes duplicates
# - Keeps only numbers divisible by 5
# - Multiplies each by 10
# - Returns the final list

print("\n#20")

numbers = [5, 10, 15, 10, 20, 25, 30, 30]

unique_numbers = set(numbers)

func_pipeline = list(
    map(
        lambda x: x * 10,
        filter(lambda x: x % 5 == 0, unique_numbers)))

print(func_pipeline)
