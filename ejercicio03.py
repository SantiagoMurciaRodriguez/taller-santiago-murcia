class buscador_maximo:
    def encontrar_maximo(arreglo):
        maximo = arreglo[0]
        for i in arreglo:
            if i > maximo:
                maximo = i
        return maximo
    arreglo = [5,2]
    print("El numero maximo de el arreglo es:", encontrar_maximo(arreglo))