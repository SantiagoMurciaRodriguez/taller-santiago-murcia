def fibonacci(n):
    lista = []
    for i in range(0, n):
        if i == 0 or i == 1:
            lista.append(1)
        else:
         lista.append(lista[-2] + lista[-1])
    return lista

n = 7
print("la secuencia fibo en terminos de n es:")
print(fibonacci(n))