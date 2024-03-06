def eliminar_repetidos(arreglo1):
    conjunto = set()
    conjunto = set(arreglo1)
    arreglo1 = list(conjunto)
    arreglo1.sort()
    return arreglo1

arreglo1 =[1,1,2,2,3,3,4,4,6,]
print(eliminar_repetidos(arreglo1))