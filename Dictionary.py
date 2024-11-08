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

