arreglo = []

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    arreglo.append(numero)

#a#
print(f"El cuarto componente es {arreglo[3]}")

#b#
arreglo_inv = []
for i in range(len(arreglo)-1, -1, -1):
    arreglo_inv.append(arreglo[i])

print(f"El arreglo invertido seria:")
for i in range(len(arreglo_inv)):
    print(arreglo_inv[i], end = " ")

#c#
producto = arreglo[0]*arreglo[-1]
print(f"\nEl producto entre el primer y ultimo componente es {producto}")

#d#
print("Se imprimen los componentes de indice impar:")
for i in range(1, len(arreglo), 2):
    print(arreglo[i], end= " ")

#e#
for i in range(0, len(arreglo), 2):
    if i == 0:
        suma = arreglo[i]
    else:
        suma += arreglo[i]
print(f"\nLa suma de los componentes de indice par es de {suma}")

#f#
for i in range(1, len(arreglo), 2):
    if i == 1:
        multiply = arreglo[i]
    else:
        multiply *= arreglo[i]
print(f"La multiplicacion de los componentes de indice impar es de {multiply}")

#g#
aux = arreglo[-1]
arreglo[-1] = arreglo[0]
arreglo[0] = aux

print(f"El arreglo con el resultante del primer y ultimo valor intercambiados es de:")
for i in range(len(arreglo)):
    print(arreglo[i], end = " ")
