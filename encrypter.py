import string
import random


chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key) 


normal_text = input("Enter a message to Encrypt: ")
cipher = ""

for letters in normal_text:
    index = chars.index(letters)
    cipher += key[index]

print(f"Encrypted message; {cipher}")


cipher_text = input("Enter a message to Dencrypt: ")
normal = ""

for letters in cipher_text:
    index = key.index(letters)
    normal += chars[index]

print(f"Decrypted message; {normal}")



