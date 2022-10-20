arreglo = []
cont = 0
numero = 2
while cont < 15:
    div = 0
    for i in range(1, numero+1):
        if (numero%i == 0):
            div += 1
    if div == 2 and i == numero:
        arreglo.append(numero)
        cont += 1
    numero += 1
print("Primeros 15 numeros primos: ")
for i in range(len(arreglo)):
    print(arreglo[i], end=" ")
