def ordenar_seleccion(arreglo):
    length = len(arreglo) - 1

    for i in range(0, length):
        pos_min = i #Mantiene la posición de valeu_min
        valeu_min = arreglo[pos_min]
        print(f"pasada {i +1}")
        for j in range(i, length):
            print(f' compara {valeu_min} > {arreglo[j + 1]}')
            if valeu_min > arreglo[j + 1]:
                valeu_min = arreglo[j + 1]
                pos_min = j + 1
        
        if pos_min != i:
            aux = arreglo[i]
            arreglo[i] = arreglo[pos_min] #valeu_min
            arreglo[pos_min] = aux
    return arreglo


arreglo = [3,1,2,5,4]
print("Antes de ordenar")
print(arreglo)
print("Después de ordenar")
print(ordenar_seleccion(arreglo))
