# writing into a file

# with open("./demo.txt", "a+") as file:  #note that w overwrites  so w+ will append or we can just use "append"
    # file.write(f"{'\n' * 5}  HellOOOOOO WorlD")

    #Word Count
count = 0
with open("./demo.txt", "r") as file: 
    # for eachline in file:
    #     count += 1
    # print(count)     #Counts lines

    # file.close()

    for eachline in file:
        words = eachline.strip().split(" ")
        for word in words:
           count += 1
    print(count)     #Counts lines
    file.close()