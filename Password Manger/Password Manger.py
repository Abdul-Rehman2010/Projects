import password_utils


password = [ ]

mode = password_utils.Passwords()


valid_inputs = ["add", "veiw", "quit"] 


while True:    
    print("To Add a New Passwrod Type 'Add' and To Veiw Previous Passwords Type 'Veiw' \n")


    opperation1 = input(">")
    opperation = opperation1.lower()


    if opperation not in valid_inputs:
        print("Enter a Valid Oppertation.\n")
        continue

    elif opperation == "add":
        mode.add()

    elif opperation == "veiw":
        mode.veiw()

    elif opperation == "quit":
        break
