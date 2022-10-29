arreglo = []
mult_3 = []
for i in range(8):
    numero = int(input("Ingresar un numero entero: "))
    if numero%2 == 0 and len(arreglo) < 6:
        arreglo.append(numero)
if len(arreglo) == 0:
    for i in range(6):
        arreglo.append(0)
while len(arreglo) < 6:
    arreglo.append(arreglo[-1])
print("Arreglo resultante: ")
for i in range(len(arreglo)):
    print(arreglo[i], end= " ")
for i in range(len(arreglo)):
    if i == 0:
        maximo = arreglo[i]
        posicion = [i]
        tot_arreglo = arreglo[i]
    else:
        tot_arreglo += arreglo[i]
        if arreglo[i] > maximo:
            maximo = arreglo[i]
            posicion = [i]
        elif arreglo[i] == maximo:
            posicion.append(i)
print(f"\nEl valor maximo del arreglo es {maximo} en la/s posicion/es:")
for i in range(len(posicion)):
    print(posicion[i], end= " ")
arreglo.sort()
for i in range(len(arreglo)):
    print("\n",arreglo[i], end= " ")
for i in range(len(arreglo)):
    if i == 0:
        tot_mult3 = arreglo[i]
    elif arreglo[i]%3 == 0:
        mult_3.append(arreglo[i])
        tot_mult3 += arreglo[i]
print("\nEl arreglo formado con los multiplos de 3 es de:")
for i in range(len(mult_3)):
    print(mult_3[i], end= " ")
prom_mult3 = tot_mult3 / len(mult_3)
prom_arreglo = tot_arreglo / len(arreglo)
if prom_mult3 == 0 or prom_arreglo == 0:
    print("\nUno de los arreglos tiene un promedio de 0, por lo que no se los puede comparar.")
elif prom_arreglo == prom_mult3:
    print("\nAmbos arreglos tienen el mismo promedio")
elif prom_arreglo > prom_mult3:
    print(f"\nEl arreglo original tiene mayor promedio ({prom_arreglo}) que el areglo de multiplos ({prom_mult3}.)")
elif prom_mult3 > prom_arreglo:
    print(f"\nEl arreglo de multiplos tiene mayor promedio ({prom_mult3}) que el arreglo original ({prom_arreglo}).")
