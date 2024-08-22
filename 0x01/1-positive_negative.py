#Python Module or script that can differentiate between positive or negative numbers

number = eval(input("Enter any number of your choice: "))  #eval is very good
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

    
