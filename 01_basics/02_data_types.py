"""
02_data_types.py
Topic: Data Type Behaviour & Operations
Goal: Understand how Python data types behave and how to manipulate them
"""

# -----------------------
# Numeric Types
# -----------------------

int_a = 10
int_b = 3

float_a = 5.5
complex_a = 4 + 5j

if __name__ == "__main__":
    print("--- Numeric Operations ---")
    print("Addition: ", int_a + int_b)
    print("Subtraction: ", int_a - int_b)
    print("Multiplication: ", int_a * int_b)
    print("Division: ", int_a / int_b)
    print("Floor Division: ", int_a // int_b)
    print("Modulo: ", int_a % int_b)
    print("Power: ", int_a ** int_b)
    
    print("Complex Real: ", complex_a.real)
    print("Complex Imaginary: ", complex_a.imag)

    print("Type Casting: ")
    print(float(int_a))
    print(int(float_a))


# -----------------------
# Strings
# -----------------------

string_example = "Hello, World"

if __name__ == "__main__":
    print("\n--- String Operations ---")
    print("First character: ", string_example[0])
    print("Last character: ", string_example[-1])
    print("Slice[0:5]: ", string_example[0:5])
    print("Length: ", len(string_example))
    print("Upper: ", string_example.upper())
    print("Replace: ", string_example.replace("World", "Python"))
    print("Split: ", string_example.split(","))

# -----------------------
# Lists (Mutable)
# -----------------------

list_example = [1, 2, 3]

if __name__ == "__main__":
    print("\n--- List Operations ----")
    list_example.append(4)
    print("Append: ", list_example)

    list_example.insert(0, 0)   # position, value
    print("Insert: ", list_example)

    list_example.pop(0) # removes and returns the n element of a list
    print("Pop: ", list_example)

    print("Slice [1:3]: ", list_example[1:3])

    # Reference behavior
    list_copy = list_example
    list_copy.append(99)
    print("Reference behaviour: ", list_example)    # list_copy & list_example point to the same memory address

    list_copy = list_example.copy() # this creates an actual new copy of list_example 


# -----------------------
# Tuples (Immutable)
# -----------------------

tuple_example = (1, 2, 3)

if __name__ == "__main__":
    print("\n--- Tuple Operations ---")
    print("Index 0: ", tuple_example[0])
    print("Slice [0:2]: ", tuple_example[0:2])

    nested_tuple = (1, [2, 3], 4)
    nested_tuple[1].append(5)
    print("Nested mutable inside immutable tuple: ", nested_tuple)

# -----------------------
# Sets (Unique, Unordered)
# -----------------------

set_a = {1, 2, 3}
set_b = {2, 3, 4}

if __name__ == "__main__":
    print("\n--- Set Oprations ---")
    print("Union: ", set_a | set_b)
    print("Intersection: ", set_b & set_b)
    print("Difference: ", set_a - set_b)

    set_a.add(10)
    print("Add: ", set_a)

    set_a.remove(1)
    print("Remove: ", set_a)

# -----------------------
# Dictionaries
# -----------------------

dict_example = {
    "name": "Joao", 
    "age": 26
    }

if __name__ == "__main__":
    print("\n--- Dictionary Operations ---")
    print("Access name: ", dict_example["name"])

    dict_example["age"] += 1
    print("Updated age: ", dict_example["age"])

    dict_example["status"] = "active"
    print("Added key: ", dict_example)

    print("Iterating dictionary: ")
    for key, value in dict_example.items():
        print(f"{key}: {value}")


# -----------------------
# Booleans
# -----------------------

if __name__ == "__main__":
    print("\n--- Boolean Behaviour ---")
    print("True and False: ", True and False)
    print("True or False: ", True or False)
    print("Not True: ", not True)
    print("Bool(0): ", bool(0))
    print("Bool(''): ", bool(''))
    print("Bool([]): ", bool([]))
    print("Bool([1]): ", bool([1]))


# -----------------------
# None Type
# -----------------------

none_example = None

if __name__ == "__main__":
    print("\n--- NoneType ---")
    if none_example is None:
        print("Value is None")
    
    print("Bool(None): ", bool(none_example))