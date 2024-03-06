def invertir_arreglo_sin_auxiliar(arr):
    """
    Invierte un arreglo de números enteros sin utilizar un arreglo auxiliar.

    Args:
        arr (list[int]): El arreglo a invertir.

    Returns:
        list[int]: El arreglo invertido.
    """
    # Utilizamos la notación de cortes para invertir el arreglo
    return arr[::-1]

# Ejemplo de uso
arreglo_original = [5, 2, 9, 1, 5, 6]
arreglo_invertido = invertir_arreglo_sin_auxiliar(arreglo_original)
print("Arreglo original:", arreglo_original)
print("Arreglo invertido:", arreglo_invertido)