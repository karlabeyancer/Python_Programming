#Printing ASCII Codes

"""
Write a program that prints the ASCII alphabets in lower case not followed by a new line

Hint (Use end inside the print statement), ord(), chr()

Instruction
You can only use one print function with string format
You can only use one loop
You are not allowed to store character in a variable
You are not allowed to import any module

"""

#Solution
 
 #1st attempt worked use only the ord() and chr() and a loop

i = 0
while i < 26: print(f'{chr(ord("a") + i)}', end=''); i += 1


# #2nd attempt worked using only the range() and chr()    

# for i in range(97,123):
#     print(chr(i),end='')  #end='' prevents a new line from being printed after each

   
# 3rd attempt worked use only the ord() and chr() and a loop and a

# print(*(chr(i) for i in range(ord('a'), ord('z') + 1)), sep='', end='') 

#4th attempt,  worked too

for i in range(26): print(f'{chr(ord("a") + i)}', end='')  #Worked... string Formatting applied


