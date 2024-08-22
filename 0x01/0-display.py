#Checking age of a user and renders a content

username = input("Enter your username: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hello {}, you have successfully logged in.".format(username))  #String formatting
else:
    print(f"Sorry {username}, your do not have access to this resource.")  #String formatting shortcut
