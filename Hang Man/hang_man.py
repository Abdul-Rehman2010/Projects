import hang_man_utils 
import randword

r = randword.rand_place

used_words = []
secret_word = r.country().lower()
secret_list = []
trys = 0
game = hang_man_utils.hang_man()

for i in secret_word:
    secret_list.append(i)


secret = secret_list.copy()


length = secret_list.__len__()

test = "_" * length

user_guess = []

for i in test:
    user_guess.append(i)

print(" ".join(test))
man = ""

while secret_list:
    guess = input("\n \nGuess A Letter: ").lower()

    if guess in secret_list:
        for i, letter in enumerate(secret):
            if letter == guess:
                user_guess[i] = guess

                
                secret_list = [letter for letter in secret_list if letter != guess]
                used_words.append(guess)


    elif guess not in secret_list and guess not in used_words:

        match trys:
            case 0:
                game.man1()
                trys += 1
                used_words.append(guess)
            case 1:
                game.man2()
                trys += 1
                used_words.append(guess)
            case 2:
                game.man3()
                trys += 1
                used_words.append(guess)
            case 3:
                game.man4()
                trys += 1
                used_words.append(guess)
            case 4:
                game.man5()
                trys += 1
                used_words.append(guess)
            case 5:
                game.man6()
                print(f"You Failed The Word Was {secret_word.capitalize()}")
                break

    elif guess in used_words:
        print("You Have Already Guessed This Letter")


    print(' '.join(user_guess))
    


