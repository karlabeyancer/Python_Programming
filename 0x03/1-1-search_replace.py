"""
 Home work
 implement the search_replace function and
 copy the list using another method
 
 Here, I used list() constructor ... for copying the list:

 """


mylist = [1, 2, 3, 5, 4, 2, 1, 1, 4, 89]

# Now, making a copy of the original list, we use arr for array
def search_replace(my_list, searchvalue, replacevalue):
    
    arr = list(my_list)   # Copying the list using the list() constructor
    
    # Here is the function implementation
    for idx, val in enumerate(arr):
        if val == searchvalue:
            arr[idx] = replacevalue
    return arr

# The function is being called
print(search_replace(mylist, 89, 6))

# Here prints the original list
print(mylist)