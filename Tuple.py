# 1. basic tuple creation
# creating a tuple
fruits = ('apple', 'banana', 'cherry')
print(fruits)

# trying to modify the tuple (will raise an error)
# fruits[0] = 'orange'

# 2. accessing elements
print(fruits[1]) # output: 'banana'
print(fruits[-1]) # output: 'cherry'

# 3. unpacking elements
colors = ('red', 'green', 'blue')
color1, color2, color3 = colors
print(color1) # output: 'red'
print(color2) # output: 'green'
print(color3) # output: 'blue'

# 4. tuple concatenation
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)
numbers_combined = numbers1 + numbers2
print(numbers_combined) # output: (1, 2, 3, 4, 5, 6)

# 5. tuple slicing
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(alphabet[:3]) # output: ('a', 'b', 'c')
print(alphabet[-3:]) # output: ('e', 'f', 'g')
print(alphabet[::2]) # output: ('a', 'c', 'e', 'g')

# 6. tuple methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4)) # output: 3
print(numbers.index(2)) # output: 1

# 7. nested tuples
nested = (1, 2, (3, 4), 5)
print(nested[2][1]) # output: 4

# tuple membership testing
colors = ('red', 'green', 'blue')
print('yellow' in colors) # output: False
print('blue' in colors) # output: True
 