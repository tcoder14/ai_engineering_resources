"""
List is a built-in data structure in Python that is used to store multiple items in a single variable. 
Lists are ordered, mutable (changeable), and allow duplicate elements. 
They can contain elements of different data types, including other lists.
"""

number_list = [1, 2, 3, 4, 5]

different_types_list = [1, "two", 3.0, [4, 5]]

"""
Features of Lists:
1. Ordered: The items in a list have a defined order, 
and that order will not change unless you explicitly modify the list.
2. Mutable: You can change, add, or remove items after the list has been created
3. Allow Duplicates: Since lists are indexed, they can have items with the same value.
"""

# Accessing List Items

# You can access list items by referring to their index number, starting from 0.
print(number_list[0])  # Output: 1

# Accessing the last item using negative indexing
print(number_list[-1])  # Output: 5

# Accessing elements in a nested list
print(different_types_list[3][0])  # Output: 4

# Adding Items to a List

# You can add items to a list using the append() method
number_list.append(6)
print(number_list)  # Output: [1, 2, 3, 4, 5, 6]

# You can also insert items at a specific index using the insert() method
different_types_list.insert(1, "new_item")
print(different_types_list)  # Output: [1, "new_item", "two", 3.0, [4, 5]]

# extending a list with another list using the extend() method
number_list.extend([7, 8, 9])

print(number_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Input a List from the User

# Use a Loop

user_list = []
n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

print("The list you entered is:", user_list)

# Use split() Method

# You can also take a single input string and split it into a list using the split() method.
list_items = input("Enter the elements of the list separated by spaces: ")
user_list_split = list_items.split()
print("The list you entered is:", user_list_split)

# Changing List Items

# You can change the value of a specific item by referring to its index
number_list[0] = 10

print(number_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing Items from a List

# You can remove a specific item from a list using the remove() method
number_list.remove(10)
print(number_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# You can also remove an item by its index using the pop() method
number_list.pop(0)
print(number_list)  # Output: [3, 4, 5, 6, 7, 8, 9]

# To remove all items from a list, you can use the clear() method
number_list.clear()
print(number_list)  # Output: []