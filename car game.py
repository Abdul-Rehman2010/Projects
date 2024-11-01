

help = '''
    start - To start the car
    stop - To stop the car
    quit - To exit

'''



start = str.lower(input("Type Help to start: "))


if start == "help":
    print (help)
    

while True:
     
    action = str.lower(input(""))

    if action == "start":
        print("Car started... Ready to go")

    elif action == "stop":
        print("Car stoped...")

    elif action == "quit":

        break

    else:
            print("Sorry I didnt Understand")

    
