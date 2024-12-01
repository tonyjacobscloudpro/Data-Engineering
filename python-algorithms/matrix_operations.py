# Code snippets have comments describing how each algorithm works, its time/space complexity, and when to use it. 

# matrix_operations.py

# 1. Matrix Addition
# - How it works: Adds corresponding elements of two matrices.
# - Time Complexity: O(m*n) where m is the number of rows and n is the number of columns.
# - Space Complexity: O(m*n) (output matrix storage).
# - When to use: Use for element-wise addition of matrices with identical dimensions.
print("1. Matrix Addition")
def matrix_addition(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Addition Result:", matrix_addition(matrix1, matrix2))

# 2. Matrix Subtraction
# - How it works: Subtracts corresponding elements of two matrices.
# - Time Complexity: O(m*n)
# - Space Complexity: O(m*n)
# - When to use: Use for element-wise subtraction of matrices with identical dimensions.
print("\n2. Matrix Subtraction")
def matrix_subtraction(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

print("Subtraction Result:", matrix_subtraction(matrix1, matrix2))

# 3. Matrix Multiplication
# - How it works: Multiplies rows of the first matrix with columns of the second matrix.
# - Time Complexity: O(m*n*p) where m, n, and p are dimensions of the matrices.
# - Space Complexity: O(m*p) (output matrix storage).
# - When to use: Use for combining transformations or linear equations.
print("\n3. Matrix Multiplication")
def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    cols2 = len(matrix2[0])
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result

matrix3 = [[1, 2], [3, 4], [5, 6]]
matrix4 = [[7, 8], [9, 10]]
print("Matrix 3:", matrix3)
print("Matrix 4:", matrix4)
print("Multiplication Result:", matrix_multiplication(matrix3, matrix4))

# 4. Transpose of a Matrix
# - How it works: Flips the rows and columns of a matrix.
# - Time Complexity: O(m*n)
# - Space Complexity: O(m*n)
# - When to use: Use to switch between row-major and column-major formats or for mathematical operations.
print("\n4. Transpose of a Matrix")
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix5 = [[1, 2, 3], [4, 5, 6]]
print("Original Matrix:", matrix5)
print("Transpose:", transpose(matrix5))

# 5. Matrix Determinant (2x2 Matrix)
# - How it works: Calculates the determinant of a 2x2 matrix.
# - Time Complexity: O(1)
# - Space Complexity: O(1)
# - When to use: Use to determine if a matrix is invertible.
print("\n5. Matrix Determinant (2x2)")
def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

matrix6 = [[4, 6], [3, 8]]
print("Matrix:", matrix6)
print("Determinant:", determinant_2x2(matrix6))

# 6. Identity Matrix
# - How it works: Creates a square matrix with 1s on the diagonal and 0s elsewhere.
# - Time Complexity: O(n^2)
# - Space Complexity: O(n^2)
# - When to use: Use as a neutral element in matrix multiplication.
print("\n6. Identity Matrix")
def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

size = 3
print(f"Identity Matrix ({size}x{size}):", identity_matrix(size))

# 7. Diagonal of a Matrix
# - How it works: Extracts the diagonal elements of a matrix.
# - Time Complexity: O(min(m, n))
# - Space Complexity: O(min(m, n))
# - When to use: Use to retrieve key elements in square or rectangular matrices.
print("\n7. Diagonal of a Matrix")
def diagonal(matrix):
    return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]

matrix7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix7)
print("Diagonal:", diagonal(matrix7))

# 8. Inverse of a 2x2 Matrix
# - How it works: Computes the inverse of a 2x2 matrix using its determinant.
# - Time Complexity: O(1)
# - Space Complexity: O(1)
# - When to use: Use for solving systems of linear equations or transformations.
print("\n8. Inverse of a 2x2 Matrix")
def inverse_2x2(matrix):
    det = determinant_2x2(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible.")
    return [[matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]]

matrix8 = [[4, 7], [2, 6]]
print("Matrix:", matrix8)
print("Inverse:", inverse_2x2(matrix8))

# End of Examples
print("\nAll matrix operation examples executed successfully!")

