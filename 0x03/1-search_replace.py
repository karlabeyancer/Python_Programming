"""
Searching and Replacing occurrences of items of a list
"""

mylist = [1, 2, 3, 5, 4, 2, 1, 1, 4, 89]
# def search_replace(my_list, searchindex, replacevalue):
    #here is a function that replaces all occurrence of a number by another

""""
This portion works by replacing index items based on index

my_list[searchindex] = replacevalue
    return my_list

print(search_replace(mylist, 2, 89))

"""
    
#Replace items based on value
# def search_replace(my_list, searchvalue, replacevalue):
    
#     for idx, val in enumerate(my_list): #
#         if val == searchvalue:
#             my_list[idx] = replacevalue
#     return my_list

# print(search_replace(mylist, 89, 98))

# print(mylist)

# this result implies that the original list is also changed

# Now, making a copy of the original list, we use arr for array
def search_replace(my_list, searchvalue, replacevalue):
    
    arr = my_list[:]   #the colon in the box bracket copies the elements of the original list into arr to be able to preserve the orginal
    
    #here is the function implementation
    for idx, val in enumerate(arr): #
        if val == searchvalue:
            arr[idx] = replacevalue
    return arr

#the function is being called
print(search_replace(mylist, 89, 98))

#here prints the original list
print(mylist)

#Implement the copying of a list using other ways HOME WOrk