def contar_ocurrencias(arr):
    """
    Cuenta las ocurrencias de cada elemento en un arreglo de números enteros.

    Args:
        arr (list[int]): El arreglo a analizar.

    Returns:
        dict: Un diccionario con los elementos como claves y el número de ocurrencias como valores.
    """
    contador = {}
    for elem in arr:
        contador[elem] = contador.get(elem, 0) + 1
    return contador

# Ejemplo de uso
arreglo = [1, 2, 3, 4, 1, 4, 1]
resultado = contar_ocurrencias(arreglo)
print("Diccionario de ocurrencias:", resultado)