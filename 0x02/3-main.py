"""
The entry point of the calculator program
"""
from calc import add
from calc import subtract
from calc import mult
from calc import div
from calc import ispow

from sys import argv, stderr   #system library  and argv will help to perform system rights

# print (pow(4,2)) 
# restrict some operators  REVISIT IN OUR NEXT CLASS

kwargs = [{"+" : add},{"-" : subtract},{"*" : mult}, {"/" : div}, {"^" : ispow}]   #Key Word Argument
result = 0
if __name__ == "__main__":
    if len(argv) == 4:
        num1 = int(argv[1])
        op = argv[2]
        num2 = int(argv[3])
        for args in kwargs:
            if op in args.keys():
                result = args[op](num1,num2)
                print(result)
                exit(0)   
        print("Invalid maths operator")   # create your own function that throws an error
        exit(1) #exit(1) means there is error exit(0) means no error

    else:
        print("Invalid number of arguments")
        exit(1)


"""
Rewrite the code above without using Kwargs
"""