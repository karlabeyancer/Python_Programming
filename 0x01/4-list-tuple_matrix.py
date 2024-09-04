# Creating a 3x3 matrix using a list
import random

matrix_list = []  # Initialize an empty list to hold the rows of the matrix
# count = random.randint(1,9)  # Start counting from 1

# here is a Loop for each row
for i in range(3):  # There are 3 rows
    row = []  # Initialize an empty list to hold the current row
    # Loop for each column
    for j in range(3):  # There are 3 columns
        count = random.randint(1,9)  # Start counting from 1
        row.append(count)  # Add the current count to the row
        # count += 1  # Increment the count for the next position
    matrix_list.append(row)  # Add the completed row to the matrix

# Converting each row from list to tuple
matrix_tuple = [tuple(row) for row in matrix_list]  # Create a list of tuples from the rows

# Printing the matrix
for row in matrix_tuple:  # Loop through each tuple (row) in the matrix
    print(row)  # Print the current row


# # Try

# matrix_list1 = [[3,2,1], [4,7,8],[6,5,9]]
# print (matrix_list1)