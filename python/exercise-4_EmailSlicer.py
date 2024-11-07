email= input("Enter your Email: ")
index= email.index("@")

username=email[:index]
domain=email[index+1:]

print(f"Your Username is: {username}")
print(f"Your Domain is: {domain}" )