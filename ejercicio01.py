class sumanumeros:
    def suma_numeros(arreglo):
        suma = 0
        for i in arreglo:
            suma+= i
        return suma
    arreglo = [1,1,1,1,1]
    print("La suma de sus numeros es", suma_numeros(arreglo))
    print(len(arreglo))