alphabet = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            ' '
            ]

code = [ 
        ".-" ,
        "-..." ,
        "-.-." ,
        "-.." ,
        "." ,
        "..-." ,
        "--." ,
        "...." ,
        ".." ,
        ".---" ,
        "-.-" ,
        ".-.." ,
        "--" ,
        "-." ,
        "---" ,
        ".--." ,
        "--.-" ,
        ".-." ,
        "..." ,
        "-" ,
        "..-" ,
        "...-" ,
        ".--" ,
        "-..-" ,
        "-.--" ,
        "--..",
        ''
        ]


def encoding():
    morse_code = []

    morse_message = input("What would you like to write in Morse Code: ").upper()

    for i in morse_message:
        if i in alphabet:
            index = alphabet.index(i)
            morse_code.append(code[index])
        else:
            print(f"The following character '{i}' can not be conerted into morse code, Try Again: ")
            continue

    morse = ""

    for i in morse_code:
        morse = " ".join(morse_code)

    print(morse)


def decode():
    message = []

    decoded_message = input("What would you like to Decode: ").upper()

    decoded_message = decoded_message.split(" ")


    for i in decoded_message:
        if i in code:
            index = code.index(i)
            message.append(alphabet[index])
        else:
            print(f"The following character '{i}' is not a reconized morse code, Try Again: ")
            continue

    decoded = ""

    for i in message:
        decoded = "".join(message).capitalize() 

    decoded = decoded.lower()

    print(decoded.capitalize())
