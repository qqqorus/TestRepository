import turtle

# f-strings
num = 1000000.00
print(f'{num:.2f}')

discount = 0.5
print(f'{discount:.0%}')

num1 = 123456789
print(f'{num1:,d}')

num2 = 12345.6789
print(f'{num2:.2e}')

num3 = 12345.6789
print(f'The number is {num3:12,.2f}')

# '<' for left alignment
# '>' for right alignment
# '^' for center alignment
print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}')
# format: [alignment][width][,][.precision][type]

# magic numbers are constant?
# amount = balance * 0.069
# named constant - it is a name that represents a value that does not change during the program's execution
# example: INTEREST_RATE = 0.069

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.mainloop
