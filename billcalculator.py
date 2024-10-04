print("Welcome to the bill calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10 12 15) "))
people = int(input("How many people will split the bill? "))
payment = round((bill * (tip / 100) + bill) / people, 2)

print(f"Each person should pay: {payment}")
