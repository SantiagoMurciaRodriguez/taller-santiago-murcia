#Ejercicio 1

pregunta1 = input("desea crear un lista vacia?: ")
if pregunta1 == "si":
    lista = []

pregunta2 = input("cuantos elementos desea agregar: ")

for i in range(int(pregunta2)):
    lista.append(int(input("agrega el valor de tu lista:")))

print(lista)


#Ejercicio 2

def eliminar_repetidos(arreglo1):
    conjunto = set()
    conjunto = set(arreglo1)
    arreglo1 = list(conjunto)
    arreglo1.sort()
    return arreglo1

arreglo1 =[1,1,2,2,3,3,4,4,6,]
print(eliminar_repetidos(arreglo1))


#Ejercicio 3

def suma_elementos(arreglo):
    contador = 0
    for i in arreglo:
        contador += i
    return contador

arreglo = [1,1,1,1]
print(suma_elementos(arreglo))

#Ejercicio 4

def comparador(arreglo1,arreglo2):
    vueltas1 = len(arreglo1) # Cuenta los valores que hay dentro de la primer lista "arreglo1"
    vueltas2 = len(arreglo2) # Cuenta los valores que hay dentro de la segunda lista "arreglo2"
    num_rep = [] # Lista vacia para ir agregando los numeros que coincidan 
    for i in range(0,vueltas1): # Primer for que va a determinar cuantas veces voy a comparar
        posicion = i 
        valori = posicion # Esta variable es para mantener el iterador "i" del segundo ciclo for
        for j in range(0,vueltas2): # Segundo for que va a hacer la comparaciones con el "arreglo2"
            if arreglo1[valori] == arreglo2[j] and arreglo1[valori] not in num_rep: #Condicion para agregar
                num_rep.append(arreglo1[valori]) # "append" es para agregar valores a la lista vacia
    if num_rep != []: #Como el ejercicio pide como resultado un booleano, pongo condicion
        return True
    else:
        return False

arreglo1 = [1,2,3,4,5]
arreglo2 = [6,6,6]
print(comparador(arreglo1,arreglo2))

#Ejercicio 5
def multiplicacion_circular(matriz):
    rows, cols = len(matriz), len(matriz[0])
    resultado = [[1] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # Multiplicación con el vecino en sentido horario
            resultado[i][j] = matriz[i][j] * matriz[(i + 1) % rows][j]

    return resultado

# Ejemplo de uso
matriz_ejemplo = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]

resultado_multiplicacion = multiplicacion_circular(matriz_ejemplo)

for fila in resultado_multiplicacion:
    print(fila)


