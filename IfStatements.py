# if statements

score = int(input("What is your score? "))
if score > 59:
    print("You passed!")
elif score == 0:
    print("warahell u r stewpid")
else:
    print("Try better next time :c")

# 1. Basic 'if-else' Example
age = int(input("Enter your age: "))

if age >= 18 and age < 60:
    print("You are an adult.")
elif age >= 60:
    print("You belong in a retirement home.")
else:
    print("You are underage! No drinking nuh uh!")

# 2. 'if-elif-else' Example
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    
# 3. Multiple Conditions with 'and' and 'or'
num = int(input("Enter a number: "))

if num > 0 and num < 10:
    print("The number is a single-digit positive number.")
else:
    print("The number is either negative or has more than one digit.")
    
# ** Explanation: **
# Here, the code checks if the number is a positive single-digit number.

# 4. Checking Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# ** Explanation: **
# This program determines if the entered number is odd or even.

# 5. Nested 'if-else'
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# ** Explanation: **
# This code checks if the number is positive, negative, or zero using nested 'if-else' statements

