def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return None  # Las dimensiones no son adecuadas para la multiplicación
    resultado = [[0] * len(matriz2[0]) for _ in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

# Ejemplo de uso
matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(matriz_a, matriz_b)
print(resultado)  # Debería imprimir [[19, 22], [43, 50]]