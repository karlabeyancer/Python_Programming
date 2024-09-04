# main - Entry Point of thr program


islower = __import__("0-islower").islowerf   #This __ refers to a magic method

if __name__ == "__main__":
    lettercheck = input("Enter any letter: ")
    print(islower(lettercheck))
    