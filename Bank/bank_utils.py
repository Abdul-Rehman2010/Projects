class bank:
    def show_balance():
        print(f"Your Current Balance Is ${balance:.2f}\n \n ")

    def deposit():
        money_deposit = float(input("How Much Would You Like To Deposite: $"))
        if money_deposit <= 0:
            print("Invalid Amount")
        
        else:
            return money_deposit
        

    def withdraw():
        money_withdraw = float(input("How Much Would You Like To Withdraw: $"))
        if money_withdraw <= 0:
            print("Invalid Amount")

        else:
            return money_withdraw

balance = 0
