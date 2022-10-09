arreglo = []
n = int(input("cargar numero de posiciones que tendra el arreglo: "))
while n < 10:
    print("debe cargar un numero mayor o igual a 10")
    n = int(input("cargar numero de posiciones que tendra el arreglo: "))
for i in range(0, n):
    arreglo.append(int(input("Indicar el valor del elemento: ")))
arreglo.sort(reverse = True)
i = 0
while i < 10:
    print(arreglo[i], end = " ")
    i+=1
