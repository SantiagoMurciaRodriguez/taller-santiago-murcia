def quicksort(arr):
    """
    Ordena un arreglo de números enteros utilizando el algoritmo Quicksort.

    Args:
        arr (list[int]): El arreglo a ordenar.

    Returns:
        list[int]: El arreglo ordenado.
    """
    if len(arr) <= 1:
        return arr  # Caso base: arreglo vacío o con un solo elemento

    # Elegimos un pivote (generalmente el último elemento)
    pivot = arr[-1]
    left, right = [], []

    # Particionamos el arreglo en dos subarreglos: uno con elementos menores o iguales al pivote,
    # y otro con elementos mayores al pivote
    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    # Llamada recursiva para ordenar los subarreglos
    return quicksort(left) + [pivot] + quicksort(right)

# Ejemplo de uso
arreglo = [5, 2, 9, 1, 5, 6]
arreglo_ordenado = quicksort(arreglo)
print("Arreglo original:", arreglo)
print("Arreglo ordenado:", arreglo_ordenado)