class buscar_numeros:
    def buscador_numeros(lista, numero):
        for num in lista:
            if num == numero:
                return True
            False
        return False
    
    arreglo = [1,3,5,7]
    numero = 2
    print("es verdad que el numero:",numero, "esta en el arreglo?:", buscador_numeros(arreglo,2))