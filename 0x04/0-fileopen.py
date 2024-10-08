"""
a module that handles the opening of a file
"""

# file = open("./demo.txt", "r")  #./ referes to parent folder

# # for line in file:
# # print(file.read(29))
# print(file.readline())   #prints a single line

with open("./demo.txt", "r") as file:
    print(file.readline())



# # Example: 0-fileopen.py  
# try:  
#     # Open the file in read mode  
#     with open('./demo.txt', 'r', encoding='cp1252') as file:  
#         # Read the content of the file  
#         content = file.read()  
#         # Print the content to the console  
#         print(content)  

# except FileNotFoundError:  
#     print("The file 'demo.txt' was not found.")  
# except Exception as e:  
#     print(f"An error occurred: {e}")  