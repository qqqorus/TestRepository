# list exercise

# making a list
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)

# list indexing
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# replacing an element
animals = ["cat", "dog", "bird"]
animals[1] = "hamster"
animals[2] = "snake"
print(animals)

# appending an element
colors = []
colors.append("red")
colors.append("green")
colors.append("blue")
print(colors)
colors.remove("green")
print(colors)

# length of a list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
length = len(names)
print(f"Length of the list: {length}")

# sum of a list
numbers = [4, 7, 1, 8, 5]
sum_of_numbers = sum(numbers)
print(f"Sum of the elements: {sum_of_numbers}") 

# maximum and minimum numbers in a list
ages = [23, 45, 18, 34, 60]
print("Maximum age: ", max(ages))
print("Minimum age: ", min(ages))

# sort a list
scores = [88, 56, 92, 78, 61]
scores.sort()
print("Sorted list: ", scores)

# check if element exists in list
numbers = [1, 3, 5, 7, 9]
user_number = int(input("Give me a number: "))
if user_number in numbers:
    print("Found")
else:
    print("Not found")

# count occurrences of an element
items = [1, 2, 2, 3, 4, 4, 4, 5]
freq_of_4 = items.count(4)
print(f"There are {freq_of_4} 4's in the list.")

# extending a list (can also use concatenation)
list1 = [3, 27, 6, 5, 26]
list2 = [1, 2, 3, 4]
list1.extend(list2)
print(list1)
list1.reverse() # reversing a list
print(list1)
