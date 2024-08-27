#Generating random by importing "random library"

"""
Question: Write a Program that will assign a random signed number to the variable number
each time it is executed.
Your Program should compute the last digit of the random number.The output of the program should be
The last digit of...followed by the number, followed by ...is... followed by the last digit...followed by
 If the last digit is greater than 5, 
Print last digit is greater than 5
If the last Digit is zero, print last digit and is zero
If the last digit less than 6 and not zero, print the string "last digit and is less than 6 not zero
"""

import random


#Generating random number between -10000 and 10000
number = random.randint(-10000, 10000)
#print(number)
#lastdigit =number / 10
lastdigit = abs(number) % 10  # Use abs to ensure last digit is positive
#last = number // 10  #interger division
#print(f"Last digit of {number} is ", end="" )   Variant of string formatting
print("the last digit of {} is ".format(number), end="")  
if lastdigit >5:
    print(f"{lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"{lastdigit} and is 0")
else:
    print(f"{lastdigit} and is less than 6 and not zero")



#print(last)


