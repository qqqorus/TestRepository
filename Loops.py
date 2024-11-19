# while loop: a condition-controlled loop
    # uses a true/false condition to control the number of times the loop iterates
    # while condition is true, do something
        # two parts:
            # condition tested for true or false value
            # statements repeated as long as condition is true
        # in a flow chart, line goes back to previous part
        # general format:
            # while [condition]:
                # [statment]
    # while loop is known as a pretest loop
    # you can write a while loop in a single line
# iteration: one execution of the body of a loop
# infinite loop: loop that does not have a way of stopping
# for loop: a count-controlled loop
    # repeats / iterates a specific number of times
        # designed to work with sequence of data items
    # the range function simplifies the 
    

# 1. print numbers from 1 - 10
for i in range(1, 11):
    print(i)
    
# 2. sum of first 5 numbers
total = 0
for i in range(1, 5):
    total += i
print(total)

# 3. print each character in a string
text = input("Enter a string: ")
for char in text:
    print(char)

# 4. count down from a given number
number = int(input("Give me a number: "))
while number >= 0:
    print(number)
    number -= 1
    
# 5. multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 6. sum of elements in a list
numbers = [3, 5, 7, 9, 11]
total = 0
for num in numbers:
    total += num
print(f"Sum of list elements: {total}")

# 7. find minimum in a list
numbers = [12, 4, 56, 17, 8]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(f"The minimum number is: {minimum}")

# 8. guess the number game
import random
target = random.randint(1, 50)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 to 50: "))
    if guess < target:
        print("Your guess is too low.")
    elif guess > target:
        print("Your guess is too high!")
print("Correct! You guessed the number!")
        

# 9. check for prime numbers
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False 
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# 10.  factorial calculation
num = int(input("Enter a positive integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}.")

# 11. calculate average of input numbers
total = 0
count = 0
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    total += int(user_input)
    count += 1
if count > 0:
    print("Average:", total / count)
else:
    print("No numbers were entered.")
    
# 12. find smallest and largest numbers
smallest = None
largest = None
while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    if user_input.lower() == 'stop':
        break
    num = int(user_input)
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
print("Smallest number:", smallest)
print("Largest number:", largest)

# 13. fibonacci sequence
n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 14. count the occurrences of each word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word occurrences:", word_count)
