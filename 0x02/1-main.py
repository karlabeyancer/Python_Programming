
addnum = __import__("1-add").funcaddnum   # Magic Method


if __name__ == "__main__":
    num1 = eval(input("Enter first positive number: "))
    num2 = eval(input("Enter second positive number: "))
    print(addnum(num1,num2))
