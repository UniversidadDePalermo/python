arreglo = []
pares = 0
impares = 0
pos_par = 0
pos_impar = 1
for i in range(10):
    i = int(input("Ingrese un numero par o impar: "))
    while pares == 5 and i%2 == 0:
            print("Ya hay demasiados numeros pares. Ingrese un impar")
            i = int(input("Ingrese un numero IMPAR: "))
    while impares == 5 and i%2 == 1:
            print("Ya hay demasiados numeros impares. Ingrese un par")
            i = int(input("Ingrese un numero PAR: "))
    if i%2 == 0:
        arreglo.insert(pos_par, i)
        pos_par += 2
        pares += 1
    elif i%2 == 1:
        arreglo.insert(pos_par, i)
        pos_impar += 2
        impares += 1
print(arreglo)
suma5pares = 0
suma5cant = 0
for i in range(len(arreglo)):
    if arreglo[i]%5 == 0 and i%2 == 0:
        suma5pares += arreglo[i]
        suma5cant += 1
promedio = suma5pares/suma5cant
if promedio == 0:
    print("No existen numeros multiplos de 5 pares en el arreglo")
elif promedio != 0:
    print(f"El promedio de los numeros multiplos de 5 en posiciones pares es de {promedio}")
suma_pares = 0
for i in range(len(arreglo)):
    if i%2 == 0:
        suma_pares += arreglo[i]
print(f"La suma de los numeros pares es de {suma_pares}")
suma4cant = 0
for i in range(len(arreglo)):
    if arreglo[i]%4 == 0:
        suma4cant += 1
print(f"La cantidad de numeros multiplos de 4 es de {suma4cant}")
for i in range(0, len(arreglo), 2):
    arreglo[i], arreglo[i+1] = arreglo[i+1], arreglo[i]
print(arreglo)
menores = 0
for i in range(0, len(arreglo), 2):
    if arreglo[i] < arreglo[i+1]:
        menores += 1
print(f"El primero es menor que el segundo en {menores} ocasiones")
