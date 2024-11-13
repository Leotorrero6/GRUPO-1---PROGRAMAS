import numpy as np

# Definimos una matriz A de 2x2
A = np.array([[1, 2], [3, 4]])
print("Matriz A:")
print(A)

# Definimos una matriz B de 2x2
B = np.array([[5, 6], [7, 8]])
print("Matriz B:")
print(B)

# Suma de matrices: A + B
suma = A + B
print("\nSuma de A y B (A + B):")
print(suma)

# Resta de matrices: A - B
resta = A - B
print("\nResta de A y B (A - B):")
print(resta)

# Multiplicación de matrices (producto punto): A * B
multiplicacion = np.dot(A, B)
print("\nMultiplicación de A y B (A * B):")
print(multiplicacion)

# Transpuesta de la matriz A
transpuesta_A = A.T
print("\nTranspuesta de A:")
print(transpuesta_A)

# Determinante de la matriz A
determinante_A = np.linalg.det(A)
print("\nDeterminante de A:")
print(determinante_A)

# Inversa de la matriz A (si el determinante es diferente de 0)
if determinante_A != 0:
    inversa_A = np.linalg.inv(A)
    print("\nInversa de A:")
    print(inversa_A)
else:
    print("\nLa matriz A no tiene inversa (su determinante es 0).")