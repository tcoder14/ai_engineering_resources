"""
Dictionary is a built-in data structure in Python that is used to store data in
key-value pairs. Dictionaries are ordered, mutable (changeable), and do not allow
duplicate keys. The values can be of any data type.
"""

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

different_types_dict = {
    "integer": 1,
    "string": "Hello",
    "float": 3.14,
    "list": [1, 2, 3],
    "tuple": (4, 5),
    "dictionary": {"city": "Dhaka"}
}

"""
Features of Dictionaries:
1. Ordered: Dictionaries maintain the order of insertion (Python 3.7+).
2. Mutable: You can add, update, or remove key-value pairs.
3. Unique Keys: Duplicate keys are not allowed. If a duplicate key is added,
   the last value overwrites the previous one.
4. Key-Value Pairs: Each item consists of a key and its corresponding value.
"""

# Accessing Dictionary Items

# Access a value using its key

print(student["name"])  # Output: Alice

# Access a value using get()

print(student.get("age"))  # Output: 20

# Access a nested dictionary

person = {
    "name": "Bob",
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh"
    }
}

print(person["address"]["city"])  # Output: Dhaka

# Adding Items to a Dictionary

student["department"] = "CSE"

print(student)
# Output:
# {'name': 'Alice', 'age': 20, 'grade': 'A', 'department': 'CSE'}

# Updating Existing Items

student["grade"] = "A+"

print(student)

# Updating Multiple Items

student.update({
    "age": 21,
    "semester": 5
})

print(student)

# Input a Dictionary from the User

# Use a Loop

user_dict = {}

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for '{key}': ")
    user_dict[key] = value

print("The dictionary you entered is:")
print(user_dict)

# Changing Dictionary Items

student["name"] = "John"

print(student)

# Removing Items from a Dictionary

# Remove a specific key using pop()

student.pop("semester")

print(student)

# Remove the last inserted key-value pair

student.popitem()

print(student)

# Remove a key using del

del student["department"]

print(student)

# Remove all items

student.clear()

print(student)  # Output: {}

# Dictionary Methods

employee = {
    "id": 101,
    "name": "Rahim",
    "salary": 50000
}

# keys()

print(employee.keys())
# Output: dict_keys(['id', 'name', 'salary'])

# values()

print(employee.values())
# Output: dict_values([101, 'Rahim', 50000])

# items()

print(employee.items())
# Output:
# dict_items([('id', 101), ('name', 'Rahim'), ('salary', 50000)])

# Copying a Dictionary

employee_copy = employee.copy()

print(employee_copy)

# Checking if a Key Exists

print("name" in employee)      # Output: True
print("address" in employee)   # Output: False

# Duplicate Keys

duplicate_dict = {
    "name": "Alice",
    "name": "Bob"
}

print(duplicate_dict)
# Output:
# {'name': 'Bob'}
# The second value overwrites the first one.