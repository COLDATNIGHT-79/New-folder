'''#1. Create a tuple, access elements, and slice:

my_tuple = ("apple", "banana", "cherry", "date")

# Access individual elements
first_fruit = my_tuple[0]  # "apple"
second_fruit = my_tuple[1]  # "banana"

# Slice to get a sub-tuple
sub_tuple = my_tuple[1:3]  # ("banana", "cherry")

print(f"First fruit: {first_fruit}")
print(f"Second fruit: {second_fruit}")
print(f"Sub-tuple: {sub_tuple}")

#2. Demonstrate tuple unpacking with multiple variables:

fruits = ("mango", "pineapple", "grapefruit")

# Unpack into variables
fruit1, fruit2, fruit3 = fruits

print(f"First fruit (unpacked): {fruit1}")
print(f"Second fruit (unpacked): {fruit2}")
print(f"Third fruit (unpacked): {fruit3}")

#3. Perform basic set operations:


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union - combines elements from both sets
union_set = set1.union(set2)

# Intersection - elements present in both sets
intersection_set = set1.intersection(set2)

# Difference - elements in set1 but not in set2
difference_set = set1.difference(set2)

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")

#4. Check if an element exists in a set:


my_set = {7, 8, 9, 10}

if 8 in my_set:
    print("Element 8 exists in the set.")
else:
    print("Element 8 not found in the set.")

#5. Create a dictionary, add key-value pairs, and access values:


fruits_dict = {"apple": "red", "banana": "yellow", "orange": "orange"}

# Add a key-value pair
fruits_dict["grape"] = "purple"

# Access value using key
apple_color = fruits_dict["apple"]

print(f"Fruits dictionary: {fruits_dict}")
print(f"Color of apple: {apple_color}")

#6. Iterate over keys and values:


fruits_dict = {"mango": "yellow", "kiwi": "green", "papaya": "orange"}

# Iterate over keys
for key in fruits_dict:
    print(f"Key: {key}")

# Iterate over values
for value in fruits_dict.values():
    print(f"Value: {value}")

# Iterate over both (key, value) pairs
for key, value in fruits_dict.items():
    print(f"Key: {key}, Value: {value}")

#7. Function with two positional arguments:


def add_numbers(num1, num2):
    """Adds two numbers and returns the sum."""
    return num1 + num2

result = add_numbers(5, 10)
print(f"Sum: {result}")

#8. Function with keyword arguments:


def print_kwargs(**kwargs):
    """Prints keyword arguments (arbitrary number)."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")

#9. Function with required and optional arguments:


def greet(name, message="Hello!"):
    """Greets someone with a name and an optional message."""
    print(f"{message}, {name}")

greet("Bob")  # Uses default message
greet("Charlie", "Welcome aboard!")

#10. Function with any number of positional arguments:

#Python
def sum_all(*numbers):
    """Calculates the sum of any number of positional arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

sum_result = sum_all(1, 2, 3, 4, 5)'''

