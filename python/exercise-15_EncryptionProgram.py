import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
running = True
encrypted_texts = []

print("------------ENCRYPTION PROGRAM------------")
while running:

    #Encryption

    plain_text = input("Enter a text to encrypt(q to quit): ")
    if plain_text == "q":
        break
    
    cypher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cypher_text += key[index]

    print(f"Original text: {plain_text}")
    print(f"Encrypted text: {cypher_text}")
    encrypted_texts.append({"plain_text": plain_text, "encrypted_text": cypher_text})

    #Decryption

    cypher_text = input("Enter a text to decrypt(q to quit): ")
    if cypher_text == "q":
        break
    plain_text= ""

    for letter in cypher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted text: {cypher_text}")
    print(f"Original text: {plain_text}")

print("--------ENCRYPTED TEXTS--------")
for i, text in enumerate(encrypted_texts, start=1):
    print(f"{i}. Plain text: {text['plain_text']}")
    print(f"   Encrypted text: {text['encrypted_text']}")
    print("-----------------------------")
    