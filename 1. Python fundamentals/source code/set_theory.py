"""
Set is a built-in data structure in Python that is used to store multiple unique items in a single variable.
Sets are unordered, mutable (changeable), and do not allow duplicate elements.
They can contain elements of different data types.
"""

number_set = {1, 2, 3, 4, 5}

different_types_set = {1, "two", 3.0, (4, 5)}

"""
Features of Sets:
1. Unordered: The items in a set do not have a fixed order.
2. Mutable: You can add or remove items after the set has been created.
3. No Duplicates: Duplicate values are automatically removed.
"""

# Duplicate values are ignored

duplicate_set = {1, 2, 2, 3, 3, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5}

# Accessing Set Items

# Sets do not support indexing or slicing.

# print(number_set[0])      # TypeError
# print(number_set[-1])     # TypeError

# You can access items by looping through the set.

for item in number_set:
    print(item)

# Check if an item exists

print(3 in number_set)   # Output: True
print(10 in number_set)  # Output: False

# Adding Items to a Set

# Add a single item using add()

number_set.add(6)
print(number_set)

# Add multiple items using update()

number_set.update([7, 8, 9])
print(number_set)

# Input a Set from the User

# Use a Loop

user_set = set()

n = int(input("Enter the number of elements you want to add to the set: "))

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_set.add(element)

print("The set you entered is:", user_set)

# Use split() Method

# You can also take a single input string and convert it into a set.

set_items = input("Enter the elements of the set separated by spaces: ")

user_set_split = set(set_items.split())

print("The set you entered is:", user_set_split)

# Adding Duplicate Values

number_set.add(5)

print(number_set)
# 5 is already present, so nothing changes.

# Removing Items from a Set

# remove() removes a specific item.
# Raises KeyError if the item does not exist.

number_set.remove(9)

print(number_set)

# discard() removes an item if it exists.
# Does NOT raise an error if the item is missing.

number_set.discard(100)

print(number_set)

# pop() removes and returns a random item.

removed_item = number_set.pop()

print("Removed:", removed_item)
print(number_set)

# clear() removes all items.

number_set.clear()

print(number_set)  # Output: set()

# Set Operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union

print(set_a.union(set_b))
# Output: {1, 2, 3, 4, 5, 6}

# Intersection

print(set_a.intersection(set_b))
# Output: {3, 4}

# Difference

print(set_a.difference(set_b))
# Output: {1, 2}

# Symmetric Difference

print(set_a.symmetric_difference(set_b))
# Output: {1, 2, 5, 6}

# Subset

print({1, 2}.issubset(set_a))
# Output: True

# Superset

print(set_a.issuperset({1, 2}))
# Output: True

# Disjoint

print({10, 11}.isdisjoint(set_a))
# Output: True