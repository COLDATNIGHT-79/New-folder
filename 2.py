import numpy as np

# Function to multiply two matrices and print the result
def multiply_matrices(n):
    # Generate two random n x n matrices
    matrix1 = np.random.rand(n, n)
    matrix2 = np.random.rand(n, n)

    # Multiply the matrices
    result_matrix = np.dot(matrix1, matrix2)

    # Print the matrices and the result
    print("Matrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)
    print("\nResult of multiplication:")
    print(result_matrix)
    print(f"\nOrder of the result matrix: {result_matrix.shape}")

# Example usage
n = 3  # Specify the order of the matrices
multiply_matrices(n)

