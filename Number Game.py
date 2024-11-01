import random

secret_number = random.randint(1,10)

trys = 0

guess = int(input("Guess the Number Between 1 and 10 : "))

while trys != 4:
    

    trys = trys+1

    if guess == secret_number:
        print("Correct you got it in" , trys , "trys")
        break

    elif secret_number != guess:
        print("Try again, you have ",(5-trys) , "trys left")

    guess = int(input("Guess the Number Between 1 and 10 : "))


if guess != secret_number:
    print("You failed, The number was : " , secret_number)
