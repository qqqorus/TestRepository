# if-else activity

# restaurant order discount
bill_amount = float(input("What is your total bill?: £"))

if bill_amount >= 50:
    discount = bill_amount * 0.1 # multiply the bill_amount with 0.1 or 10% in decimal to get the discount
    bill_amount = bill_amount - discount # subtract the bill_amount from the discount to get the final bill
    print(f"Discount applied. Your total bill is £{bill_amount:.2f}.") # using .2f to round the final bill_amount to 2 decimal places
else:
    print(f"No discount applied. Your total bill is £{bill_amount:.2f}.")
    
# movie ticket price
age = int(input("How old are you?: "))

if age <= 12:
    print("Your ticket price is £5")
elif age > 12 and age <= 17:
    print("Your ticket price is £7")
elif age > 17 and age <= 64:
    print("Your ticket price is £10")
else:
    print("Your ticket price is £6")

# bank withdrawal
account_bal = float(input("Account Balance: "))
withdrawal_amount = float(input("How much will you want to withdraw?: "))

if account_bal <= withdrawal_amount:
    print("You cannot withdraw. Your account balance is low.")
else:
    balance_left = account_bal - withdrawal_amount
    if balance_left >= 1000:
        print(f"You have successfully withdrawn {withdrawal_amount}. Your remaining balance is {balance_left}. Thank you for using our service.")
    if balance_left <= 100:
        print(f"You have successfully withdrawn {withdrawal_amount}. Your remaning balance is {balance_left} and is a low-balance.")