"""
Tuple is a built-in data structure in Python that is used to store multiple items in a single variable.
Tuples are ordered, immutable (cannot be changed after creation), and allow duplicate elements.
They can contain elements of different data types, including other tuples.
"""

number_tuple = (1, 2, 3, 4, 5)

different_types_tuple = (1, "two", 3.0, (4, 5))

"""
Features of Tuples:
1. Ordered: The items in a tuple have a defined order.
2. Immutable: You cannot change, add, or remove items after the tuple has been created.
3. Allow Duplicates: Tuples can contain multiple items with the same value.
"""

# Accessing Tuple Items

# You can access tuple items by referring to their index number, starting from 0.
print(number_tuple[0])  # Output: 1

# Accessing the last item using negative indexing
print(number_tuple[-1])  # Output: 5

# Accessing elements in a nested tuple
print(different_types_tuple[3][0])  # Output: 4

# Tuple Methods

# count() returns the number of times a value appears
sample_tuple = (1, 2, 2, 3, 2, 4)
print(sample_tuple.count(2))  # Output: 3

# index() returns the index of the first occurrence
print(sample_tuple.index(3))  # Output: 3

# Input a Tuple from the User

# Use a Loop

user_list = []
n = int(input("Enter the number of elements you want to add to the tuple: "))

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

user_tuple = tuple(user_list)

print("The tuple you entered is:", user_tuple)

# Use split() Method

# You can also take a single input string and split it into a tuple.
tuple_items = input("Enter the elements of the tuple separated by spaces: ")

user_tuple_split = tuple(tuple_items.split())

print("The tuple you entered is:", user_tuple_split)

# Changing Tuple Items

# Tuples are immutable.
# The following line will raise a TypeError.

# number_tuple[0] = 10
# TypeError: 'tuple' object does not support item assignment

# Adding Items to a Tuple

# Tuples cannot be modified directly.
# You can create a new tuple by concatenation.

number_tuple = number_tuple + (6,)
print(number_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Extending a Tuple

number_tuple = number_tuple + (7, 8, 9)
print(number_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Removing Items from a Tuple

# Tuples do not support remove(), pop(), or clear() methods.

# number_tuple.remove(1)   # AttributeError
# number_tuple.pop()       # AttributeError

# To remove an item, convert the tuple to a list.

temp_list = list(number_tuple)

temp_list.remove(5)

number_tuple = tuple(temp_list)

print(number_tuple)  # Output: (1, 2, 3, 4, 6, 7, 8, 9)

# Clearing a Tuple

# Since tuples are immutable, you cannot clear them.
# You can create an empty tuple instead.

number_tuple = ()
print(number_tuple)  # Output: ()