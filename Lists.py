# lists

# sequence - an object that contains multiple items of data
# e.g. lists and tuples
# list - an object that contains multiple data items
# element - is an item in a list
# list() can convert certain types of objects to lists

marks = [20, 40, 60, 80, 100, 27, 50, 33, 79]
print(len(marks))

even_numbers = [2, 4, 6, 8, 10]
names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adriana']
info = ['Adriana', 27, 1550.87]

print(even_numbers)
print(names)
print(info)

# repitition operator - makes multiple copies of a list and joins them together
# the * symbol is a repetition operator when applied to a sequence and an integer
# general format: list * n
# you can iterate over a list using a for loop, format: for x in list:

# index - a number specifying the position of an element in a list
# index of first item is 0, second element is 1, and the n'th element is -1
# negative indexes identify positions relative to the end of the list
# the index -1 identifies the last element, -2 identifies the next to last element, etc.

# len function - returns the length of a sequence such as a list

# concatenate - joining two lists together
# the + operator can be used to concatenate two lists
# cannot concatenate a list with another data type, such as a number
# the '+=' augmented assignment operator can also be used to concatenate lists

# slice - 
list = [2, 25, 67, 89, 25]
print(list[:2])