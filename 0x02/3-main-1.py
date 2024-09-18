"""
The entry point of the calculator program
"""
from calc import add
from calc import subtract
from calc import mult
from calc import div
from calc import ispow

from sys import argv, stderr   # system library and argv will help to perform system rights

# The main calculator logic
if __name__ == "__main__":
    if len(argv) == 4:
        num1 = int(argv[1])
        op = argv[2]
        num2 = int(argv[3])
        
        # Initialize result variable
        result = 0
        
        # Determine which operation to perform
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = mult(num1, num2)
        elif op == "/":
            result = div(num1, num2)
        elif op == "^":
            result = ispow(num1, num2)
        else:
            print("Invalid math operator")  # create your own function that throws an error
            exit(1)  # exit(1) means there is an error; exit(0) means no error
        
        print(result)
        exit(0)  # Successful execution

    else:
        print("Invalid number of arguments")
        exit(1)