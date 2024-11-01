import bank_utils

u = bank_utils

money_withdraw = 0
money_deposit = 0
balance = 0
b = u.bank

while True:

    operation = input("What Would You Like to Do:   ").lower()

    if operation not in ["withdraw", "deposit", "balance"]:
        print("Invalid Opption Please Try Again.")
        continue

    match operation:
        case "deposit":
            balance += b.deposit()
            print(f"Current Balance is ${balance:.2f} \n \n")

        case "withdraw":
            balance -= b.withdraw()
            if balance < 0:
                print("You Are In Debt.")
                print(f"Current Balance is ${balance:.2f} \n \n")

            else:
                print(f"Current Balance is ${balance:.2f} \n \n")

        case "balance":
            if balance < 0:
                print("You Are In Debt.")
                b.show_balance()
                
            else:
                b.show_balance()

