#-------------------------------------------------
print("#1")
print()

def generator_numbers():
    number = 1

    while number < 4:
        yield number
        number += 1

gen = generator_numbers()
print(next(gen))
print(next(gen))
print(next(gen))

print()

#-------------------------------------------------
print("#2")
print()

def generator_string():
    text = "PYTHON"
    current_char = 0

    while current_char < len(text):
        yield text[current_char]
        current_char += 1

gen = generator_string()
print(next(gen))
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#3")
print()


def gen_numbers(numbers):
    current_num = 0

    while current_num < len(numbers):
        yield numbers[current_num]
        current_num += 1

numbers = [1, 2, 3, 4]

gen = gen_numbers(numbers)
for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#4")
print()

def function_return():
    return 1
    return 2

print(function_return())

print()


#-------------------------------------------------
print("#5")
print()

def function_yield():
    yield 1
    yield 2

gen = function_yield()
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#6")
print()

def gen_start():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("Stop")
    yield 3

gen = gen_start()

print(next(gen))
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#7")
print()

def count_up_to(limit):
    current = 1

    while current <= limit:
        yield current
        current += 1

gen = count_up_to(5)
for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#8")
print()

def count_up_to_step(start, stop, step):
    current = start

    while current < stop:
        yield current
        current += step

gen = count_up_to_step(0, 10, 2)

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#9")
print()

def gen_squares():
    current = 1

    while current <= 5:
        yield current ** 2
        current += 1

gen = gen_squares()

print(type(gen))

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#10")
print()

def gen_filter(numbers):
    for num in numbers:
        if num > 10:
            yield num

numbers = [5, 12, 17, 3]
gen = gen_filter(numbers)

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#11")
print()

def infinite_counter():
    current = 1

    while True:
        yield current
        current += 1

gen = infinite_counter()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#12")
print()

def infinite_even_number():
    current = 0

    while True:
        if current % 2 == 0: yield current
        current += 1

gen = infinite_even_number()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#13")
print()

def gen_lines():
    current = 0

    while True:
        yield f"Line {current}"
        current += 1

gen = gen_lines()

print(next(gen))
print(next(gen))
print(next(gen))

print()


#-------------------------------------------------
print("#14")
print()

list_example = [i for i in range(10_000_000)]
gen_example = (i for i in range(10_000_000))

print(type(list_example))
print(type(gen_example))

print()

# A list has all its elements in memory
# A generator only has them in memory when you iterate through them

#-------------------------------------------------
print("#15")
print()

def multiply_by_two(numbers):
    current = 0

    while current < len(numbers):
        yield numbers[current] * 2
        current += 1

def filter_even(numbers):
    current = 0

    while current < len(numbers):
        if numbers[current] % 2 == 0: yield numbers[current]
        current += 1

numbers = [1, 2, 3, 4, 5]

gen_multi = multiply_by_two(numbers)

multiplied = []
for num in gen_multi:
    multiplied.append(num)

gen_even = filter_even(multiplied)

for num in gen_even:
    print(num)

print()


#-------------------------------------------------
print("#16")
print()

def gen_fibonacci(limit):
    position = 0
    current = 0
    previous = 0

    while position < limit:
        if position <= 1:
            current = position
            position += 1
            yield current
        else:
            temp = previous
            previous = current
            current = current + temp
            yield current
            position += 1

gen = gen_fibonacci(7)

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#17")
print()

def factorial_generator(n):
    counter = 1
    previous = 1

    while counter <= n:
        previous = counter * previous
        yield previous
        counter += 1

gen = factorial_generator(5)

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#18")
print()

def gen_reverse(numbers):
    current = len(numbers) - 1

    while current >= 0:
        yield numbers[current]
        current -= 1

numbers = [1, 2, 3]

gen = gen_reverse(numbers)

for num in gen:
    print(num)

print()


#-------------------------------------------------
print("#19")
print()

def repeat_value(value, times):
    current = 1

    while current <= times:
        yield value
        current += 1

gen = repeat_value("A", 3)

for value in gen:
    print(value)

print()


#-------------------------------------------------
print("#20")
print()

def gen_range(start, stop, step):
    current = start

    while current < stop:
        yield current
        current += step

gen = gen_range(0, 10, 2)

for num in gen:
    print(num)


print()
