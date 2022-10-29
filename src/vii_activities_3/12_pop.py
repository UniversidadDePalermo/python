arreglo = []
for i in range (10):
    arreglo.append(int(input("Ingrese el elemento: ")))
arreglo.pop(0)
for i in range(len(arreglo)):
    print(arreglo[i], end=" ")
