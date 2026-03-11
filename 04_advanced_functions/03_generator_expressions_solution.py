# ------------------
# Basic Generator Expressions
# ------------------

# 1. Create a generator expression that yields numbers 0 to 4
# Use a for loop to print all values

print("#1")

gen_exp = (x for x in range(5))

for num in gen_exp:
    print(num)

print()


# 2. Create a generator expression that yields the squares of numbers 1 to 5
# Print all results

print("#2")

gen_exp = (x ** 2 for x in range(1, 6))

for num in gen_exp:
    print(num)

print()

# 3. Create a generator expression from a string "PYTHON"
# Yield each character in the string using a for loop

print("#3")

gen_exp = (char for char in "PYTHON")

for char in gen_exp:
    print(char)

print()


# ------------------
# Generator Expressions With Conditions
# ------------------

# 4. Create a generator expression that yields only even numbers from 0 to 9
# Print all results

print("#4")

gen_exp = (x for x in range(10) if x % 2 == 0)

for num in gen_exp:
    print(num)

print()


# 5. Create a generator expression that yields the squares of only odd numbers from 1 to 10
# Print all results

print("#5")

gen_exp = (x ** 2 for x in range(1, 11) if x % 2 != 0)

for num in gen_exp:
    print(num)

print()

# 6. Filter a list [5, 12, 7, 20, 3] using a generator expression to yield numbers > 10
# Print all results

print("#6")

numbers = [5, 12, 7, 20, 3]

gen_exp = (x for x in numbers if x > 10)

for num in gen_exp:
    print(num)

print()


# ------------------
# Nested Generator Expressions
# ------------------

# 7. Create a nested generator expression that yields pairs (i, j)
# for i in range(3) and j in range(2)
# Print all pairs

print("#7")

gen_exp = ((i, j) for i in range(3) for j in range(2))

for pair in gen_exp:
    print(pair)

print()

# 8. Create a nested generator expression that yields the sum i + j
# for i in range(3) and j in range(2)
# Print all sums

print("#8")

gen_exp = (i + j for i in range(3) for j in range(2))

for num in gen_exp:
    print(num)

print()


# 9. Generate all combinations of letters from 'AB' and 'XY' using a generator expression
# Print each combination

print("#9")

gen_exp = ((i, j) for i in "AB" for j in "XY")

for pair in gen_exp:
    print(pair)

print()

# ------------------
# Using Generator Expressions With Functions
# ------------------

# 10. Use a generator expression with sum() to compute the sum of squares from 1 to 5
# Print the result

print("#10")

gen_exp = sum(x ** 2 for x in range(1, 6))
print(gen_exp)

print()


# 11. Use a generator expression with max() to find the maximum square of numbers 1 to 10
# Print the result

print("#11")

gen_exp = max(x ** 2 for x in range(1, 11))
print(gen_exp)

print()


# 12. Use a generator expression with min() to find the minimum odd number in range 1 to 10
# Print the result

print("#12")

gen_exp = min(x for x in range(1, 11) if x % 2 != 0)
print(gen_exp)

print()


# ------------------
# Memory Efficiency
# ------------------

# 13. Create a list comprehension of squares from 0 to 999_999
# Create a generator expression of the same
# Print the type of both
# Optionally, print memory usage using sys.getsizeof()

print("#13")

import sys

list_example = [x for x in range(1_000_000)]
gen_exp = (x for x in range(1_000_000))

print(type(list_example))
print(type(gen_exp))

print(sys.getsizeof(list_example))
print(sys.getsizeof(gen_exp))

print()


# ------------------
# Generator Pipelines
# ------------------

# 14. Create a generator expression that multiplies numbers 1 to 5 by 2
# Pipe it into another generator expression that filters only numbers > 5
# Print all results

print("#14")

gen_multi = (x * 2 for x in range(1, 6))
gen_filter = (x for x in gen_multi if x > 5)

for num in gen_filter:
    print(num)

print()


# 15. Create a generator pipeline that squares numbers 1 to 10, then keeps only numbers divisible by 3
# Print all results

print("#15")

gen_square = (x ** 2 for x in range(1, 11))
gen_div = (x for x in gen_square if x % 3 == 0)

for num in gen_div:
    print(num)

print()


# ------------------
# Thinking Like Python
# ------------------

# 16. Rewrite a Fibonacci generator using a generator expression (hint: you may need to use a helper function)
# Generate first 7 Fibonacci numbers
# Print all values

print("#16")

def calc_fib(n):
    previous, current = 0, 1

    for i in range(n):
        previous, current = current, previous + current

    return previous

gen_fibonacci = (calc_fib(x) for x in range(7))

for num in gen_fibonacci:
    print(num)

print()


# 17. Create a generator expression that yields factorials from 1! to 5!
# Print all results

print("#17")

def fact(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

gen_exp = (fact(x) for x in range(1, 6))

for num in gen_exp:
    print(num)

print()


# ------------------
# Advanced Challenges
# ------------------

# 18. Flatten a list of lists [[1, 2], [3, 4], [5]] using a generator expression
# Print all values

print("#18")

list_lists = [[1, 2], [3, 4], [5]]

gen_exp = (element for sublist in list_lists for element in sublist)

for num in gen_exp:
    print(num)

print()


# 19. Create a generator expression that yields only prime numbers from 2 to 20
# Print all results

print("#19")

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


gen_exp = (x for x in range(2, 21) if is_prime(x))

for num in gen_exp:
    print(num)

print()

# 20. Combine multiple generator expressions:
# - Generate numbers 1 to 5
# - Multiply each by 2
# - Filter results > 5
# - Square the remaining numbers
# Print all results


print("#20")

gen_numbers = (x for x in range(1, 6))
gen_multi = (num * 2 for num in gen_numbers)
gen_filter = (num for num in gen_multi if num > 5)
gen_square = (num ** 2 for num in gen_filter)
for num in gen_square:
    print(num)

print()
