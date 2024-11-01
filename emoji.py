
key = """
    :) : 😁
    :( : 😭 
    ;) : 😉
    ") : 😏 
    :] : 😐 
    :| : 😑 
"""

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😁" ,
        ":(" : "😭" , 
        ";)" : "😉" ,
        '")' : "😏" , 
        ":]" : "😐" , 
        ":|" : "😑" 
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print("choose an emoji from the key and use it in ur sentence.")
print(key)
print("to stop code type 'exit'. ")


while input != "exit":

    print(emoji_converter(input(">")))
