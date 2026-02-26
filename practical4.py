1-----
import numpy as np

# Create 4x4 identity matrix
identity_matrix = np.identity(4)

print("4x4 Identity Matrix:")
print(identity_matrix)

2-----
import numpy as np

# Generate two 3x3 matrices with random integers from 1 to 9
matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)


Lab assignment 2---------
import numpy as np

print("Enter elements for 5x3 matrix:")
matrix1 = []
for i in range(5):
    row = []
    for j in range(3):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix1.append(row)

print("\nEnter elements for 3x2 matrix:")
matrix2 = []
for i in range(3):
    row = []
    for j in range(2):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix2.append(row)

# Convert to NumPy arrays
A = np.array(matrix1)
B = np.array(matrix2)

# Matrix multiplication
product = np.dot(A, B)

print("\n5x3 Matrix:")
print(A)

print("\n3x2 Matrix:")
print(B)

print("\nProduct Matrix (5x2):")
print(product)
