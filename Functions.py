# function structure
    # def - function definition; specifies what function does
    # def [function_name]](function, arguments, or parameters):
        # statement
        # statement
    # return - returns the value back to the function
    # [name of function](function, parameters) - calls the function

# function: group of statements within a program that perform a specific task
    # usually one task of a large program
    # known as divide and conquer approach
# modularized program: program wherein each task within the program is in its own function

# void function: simply executes the staments it contains and then terminates
# value-returning function: executes the statements it contains, and then it returns a value back to the statement that called it
    # the input, int, and float functions are examples of value-returning functions

# 1. greet a user
def greet_user(name):
    """Greets the user with their name."""
    return f"Hello, {name}! Welcome to Python programming."

# Example
print(greet_user("Yoji"))

# 2. add two numbers
def sum(num1, num2, num3):
    """Adds two numbers and returns the result."""
    return num1 + num2 + num3

# Example
print(sum(327, 503, 143))

# 3. check even or odd
def check_even_odd(number):
    """Checks if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

# Example
print(check_even_odd(27))
print(check_even_odd(3))

# 4. find the largest number
def find_largest(num1, num2, num3):
    """Finds and returns the largest of three numbers."""
    return max(num1, num2, num3)

# Example
print(find_largest(27, 5, 8))

# 5. calculate factorial
def calculate_factorial(n):
    """Calculates the factorial of a number."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example
print(calculate_factorial(7))

# activity: make function that will show the avg of 4 numbers
def average(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    return sum / 4

num1 = float(input("What is your 1st grade: "))
num2 = float(input("What is your 2nd grade: "))
num3 = float(input("What is your 3rd grade: "))
num4 = float(input("What is your 4th grade: "))
print(f"Your average is: {average(num1, num2, num3, num4)}")

# 6. reverse a string
def reverse_string(text):
    """Reverses the input string."""
    return text[::-1]

# Example
print(reverse_string("Yoji"))

# 7. check prime number
def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example
print(is_prime(7))
print(is_prime(10))

# 8. count vowels in a string
def count_vowels(text):
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("I love Python programming."))

# 9. find the maximum in a list
def find_max_in_list(numbers):
    """Finds the maximum number in a list."""
    return max(numbers)

# Example
print(find_max_in_list([3, 5, 2, 9, 1]))


# 10. convert temperature
def convert_temperature(temperature, scale):
    """Converts temperature between Celsius and Fahrenheit."""
    if scale == "C":
        return (temperature * 9/5) + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (temperature - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid scale"

# Example
print(convert_temperature(0, "C"))  # Celsius to Fahrenheit
print(convert_temperature(32, "F"))  # Fahrenheit to Celsius