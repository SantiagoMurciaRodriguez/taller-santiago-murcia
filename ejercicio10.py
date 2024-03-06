def encontrar_posicion_subcadena(cadena, subcadena):
    """
    Busca la posición de la subcadena dentro de la cadena principal.

    Args:
        cadena (str): La cadena principal.
        subcadena (str): La subcadena a buscar.

    Returns:
        int: La posición de la subcadena o -1 si no se encuentra.
    """
    posicion = cadena.find(subcadena)
    return posicion

# Ejemplo de uso
cadena_principal = "Hola, ¿cómo estás? ¡Hola!"
subcadena_buscar = "¡Hola!"
posicion_encontrada = encontrar_posicion_subcadena(cadena_principal, subcadena_buscar)
print(f"La subcadena '{subcadena_buscar}' se encuentra en la posición {posicion_encontrada}")