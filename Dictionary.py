# list = []
# tuple = ()
# dicionary = {}
# syntax - dict1 = {key1 : "value"}
# dictionaries are mutable

# 1. basic dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

print(student["name"])
print(student["age"])
print(student["courses"][1])

# 2. creating dictionaries
    # using curly braces
student_info = {
    "name": "Bob",
    "age": 21,
    "major": "Computer Science"
}

# using dict() function
student_info2 = dict(name = "Emma", age = 22, major = "Biology")

print(student_info)
print(student_info2)

# 3. accessing dictionary elements
    # accessing values using keys
    # the .get() method for safe access
students = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}

# accessing using key
print(student["name"]) # output: Charlie

# using .get() to access key safely
print(student.get("GPA", "Not Available")) # output: Not Available

# 4. modifying dictionary elements
    # adding new key-value pairs
    # modifying existing values
    # removing elements using del, .pop(), and .popitem()

student = {
    "name": "Dave",
    "age": 20,
    "major": "Chemistry"
}

# adding a new key-value pair
student["GPA"] = 3.8

# modifying an existing key-value pair
student["age"] = 21

# removing a key-value pair
student.pop("major")

print(student)

# 5. dictionary methods and operations
    # important dictionary methods: .keys(), .values(), .items()
    # looping through dictionaries
    # check if a key exists using in keyword

student = {
    "name": "Eve",
    "age": 22,
    "major": "Biology"
}

# Using .keys(), .values(), and .items()
print(student.keys())    # Output: dict_keys(['name', 'age', 'major'])
print(student.values())  # Output: dict_values(['Eve', 22, 'Biology'])
print(student.items())   # Output: dict_items([('name', 'Eve'), ('age', 22), ('major', 'Biology')])

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Check if a key exists
if "GPA" in student:
    print("GPA is:", student["GPA"])
else:
    print("GPA key not found")
    
# 6. nesting dictionaries
school = {
    "student1": {"name": "Alice", "age": 20, "GPA": 3.9},
    "student2": {"name": "Bob", "age": 21, "GPA": 3.6},
}

# Accessing nested dictionary values
print(school["student1"]["name"])  # Output: Alice
print(school["student2"]["GPA"])   # Output: 3.6

# 7. real-world application of dictionaries 
inventory = {
    "item1": {"name": "Laptop", "price": 1200, "stock": 10},
    "item2": {"name": "Smartphone", "price": 800, "stock": 15},
}

# Checking stock for each item
for item_id, details in inventory.items():
    print(f"{details['name']}: ${details['price']} - {details['stock']} in stock")

# 8. class activity: building a contact list
# Starting code
contacts = {}

# Add a contact
contacts["Alice"] = {"phone": "123-456-7890", "email": "alice@example.com"}

# Allow students to expand by adding more contacts, modifying, or deleting them
