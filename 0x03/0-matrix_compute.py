
"""
This module performs matrix computation
"""

matrixlist = [[1, 2, 4], [3, 5, 6], [9, 8, 7]]
# compute the square of each element of the matrix

# def matrix_pow(matrix, pow):
#     # Here a function that takes in a pwer and returns an new matrix
#     # where each element is the square of the corresponding element in the input matrix

#     result = []   # empty list
#     for row in matrix:
#         finalmatrix = []
#         for col in row:
#             finalmatrix.append(col**pow)  # square each element
#         result.append(finalmatrix)
#     return result


def matrix_pow(matrix, pow):
    # Here a function that takes in a pwer and returns an new matrix
    # where each element is the square of the corresponding element in the input matrix

    result = [[col**pow for col in row] for row in matrix]
    return result






if __name__== "__main__":
    print(matrix_pow(matrixlist, 2))

    
# Rewrite the Matrix power using lamda and map ---Thu helps to minimize code
