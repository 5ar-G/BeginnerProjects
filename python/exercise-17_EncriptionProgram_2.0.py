import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt_text(plain_text):
    cypher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cypher_text += key[index]
    return cypher_text

def decrypt_text(cypher_text):
    plain_text = ""
    for letter in cypher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

def list_encrypted_texts(encrypted_texts):
    print("----------LIST----------")
    for i, text in enumerate(encrypted_texts, start=1):
        print(f"{i}. {text['plain_text']:15}: {text['encrypted_text']}")
       
        print()

def main():
    encrypted_texts = []
    while True:
        print("------------ENCRYPTION PROGRAM------------")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. List all encrypted texts")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("--------------------------------------")
            plain_text = input("Enter a text to encrypt: ")
            cypher_text = encrypt_text(plain_text)
            print("--------------------------------------")
            print(f"Original text: {plain_text}")
            print(f"Encrypted text: {cypher_text}")
            encrypted_texts.append({"plain_text": plain_text, "encrypted_text": cypher_text})

        elif choice == "2":
            print("--------------------------------------")
            cypher_text = input("Enter a text to decrypt: ")
            plain_text = decrypt_text(cypher_text)
            print("--------------------------------------")
            print(f"Decrypted text: {cypher_text}")
            print(f"Original text: {plain_text}")

        elif choice == "3":
            list_encrypted_texts(encrypted_texts)

        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()