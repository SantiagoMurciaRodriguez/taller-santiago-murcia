def Bubble_sort(arreglo):
    lenght = len(arreglo) - 1
    print(lenght)
    for i in range(0,lenght):
        for j in range(0,lenght):
            if arreglo[j] > arreglo[j + 1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = aux
    return arreglo
arreglo = [60,0,2,45,70,90]
print("Antes de ordenar")
print(arreglo)
print("Después de ordenar")
print(Bubble_sort(arreglo))