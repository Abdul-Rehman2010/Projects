import random



class dice:
    def one():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |       O       |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,
    
        return " "
        
    def two():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |       O O     |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,
        
        return " "

    def three():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |      O  O     |\n" ,
            "  |        O      |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,

        return " "
    
    def four():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |      O O      |\n" ,
            "  |      O O      |\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,

        return " "

    def five():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |      O O      |\n" ,
            "  |       O       |\n" ,
            "  |      O O      |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,
    
        return " "
            
    def six():
        print("    _______________\n" ,
            "  |               |\n" ,
            "  |               |\n" ,
            "  |      O O      |\n" ,
            "  |      O O      |\n" ,
            "  |      O O      |\n" ,
            "  |               |\n" ,
            "  _________________\n") ,

        return " "  


def roll():
   while True:

    user = input("Do u want to roll? (q to Quit)\n").lower()  


    while True:
        if user == "roll" or user == "q":
            break

        else:
            print("Invalid Input")
            user = input("Do u want to roll? (q to Quit)\n").lower() 
            continue

    

    if user == "roll": 

        dice_roll = random.randint(1,6)
        if dice_roll == 1:
            print(dice.one())

        elif dice_roll == 2:
            print(dice.two())

        elif dice_roll == 3:
            print(dice.three())

        elif dice_roll == 4:
            print(dice.four())

        elif dice_roll == 5:
            print(dice.five())

        elif dice_roll == 6:
            print(dice.six())

    elif user == "q":
        return " "
        break

