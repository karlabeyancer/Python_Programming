"""
This module performs matrix computation using map and lamda
"""

matrixlist = [[1, 2, 4], [3, 5, 6], [9, 8, 7]]

def matrix_pow(matrix, pow):
    # Using map and lambda to raise each element of the matrix to the specified power
    return [list(map(lambda x: x ** pow, row)) for row in matrix]

# Example usage
squared_matrix = matrix_pow(matrixlist, 2)
print("Squared Matrix:")
print(squared_matrix)

