# morse cord

import morse_utils
u = morse_utils

valid_inputs = ["encode", "decode", "q"]

while True:
    operation = input("Would you like to Encode or Decode (q to quit):  ").lower()
    
    print()
    print()

    if operation not in valid_inputs:
        print("Invalid Input, Try Again. \n\n")
        continue
    
    if operation == "encode":
        u.encoding()

    elif operation == "decode":
        u.decode()

    elif operation == "q":
        break
