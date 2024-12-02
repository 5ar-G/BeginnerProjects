import random
import string
all_characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter the length of the password: "))

if length < 8:
    print("Password length should be at least 8 characters.")
   
else:   
    password = ''.join(random.choice(all_characters) for i in range(length))
    print("---------------------------------------")
    print(f"Generated Password : {password}")
    print("---------------------------------------")