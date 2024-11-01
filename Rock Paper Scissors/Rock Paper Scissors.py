import random
import rps_utils

Rock = rps_utils.Rock
Paper = rps_utils.Paper
Scissors = rps_utils.Scissors

opptions = [ "rock" , "paper" , "scissors"]
opptions2 = [ "rock" , "paper" , "scissors" , "quit"]

player_points = 0
computer_points = 0


while True:
    player_choice = input("Rock, Paper or Scissors? ")
    player_choice = player_choice.lower()
    computer_choice = random.choice(opptions)

    if player_choice not in opptions2:
        print("Select a Valid Option")
        continue

    match player_choice:
        case "rock":
            match computer_choice:
                case "rock":
                    Rock.rock()
                
                case "paper":
                    Rock.paper()
                    computer_points = computer_points + 1

                case "scissors":
                    Rock.scissors()
                    player_points = player_points + 1
    
        case "paper":
                match computer_choice:
                    case "rock":
                        Paper.rock()
                        player_points = player_points + 1
                    
                    case "paper":
                        Paper.paper()

                    case "scissors":
                        Paper.scissors()
                        computer_points = computer_points + 1
        
        case "scissors":
                match computer_choice:
                    case "rock":
                        Scissors.rock()
                        computer_points = computer_points + 1
                    
                    case "paper":
                        Scissors.paper()
                        player_points = player_points + 1

                    case "scissors":
                        Scissors.scissors()


        case "quit":
            break



print("You Got", player_points, "Points")
print("Computer Got", computer_points, "Points")


if computer_points > player_points:
    print("Computer Wins!!!")
elif player_points > computer_points:
    print("You Win!!!")
else:
    print("Draw!!!")


