import numpy as np

print("4x4 Identity Matrix:")
identity_matrix = np.eye(4)
print(identity_matrix)

print("\n3x3 Matrix Operations:")

matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)