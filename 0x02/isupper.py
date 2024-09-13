# A module tha implements IsUpper Function
# It checks if a letter is in Upper Case or returns False otherwise

def isupper(char):
    lt = ord(char)
    # This function takes in a character and return a Boolean
    # if ord(char) >= 65 and ord(char) <= 90
    if lt >= 65 and lt <= 90:
       return True
    return False