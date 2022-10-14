arreglo = []
max_mult2 = 0
max_pos = []
min_imp = 0
min_pos = []
for i in range(4):
    i = int(input("Ingresar un numero: "))
    arreglo.append(i)
print(arreglo)
for i in range(len(arreglo)):
    if max_mult2 == 0 and arreglo[i]%2 == 0:
        max_mult2 = arreglo[i]
        max_pos.append(i)
    elif arreglo[i]%2 == 0 and arreglo[i] > max_mult2:
        max_mult2 = arreglo[i]
        max_pos = []
        max_pos.append(i)
    elif arreglo[i]%2 == 0 and arreglo[i] == max_mult2:
        max_pos.append(i)
if max_mult2 == 0:
    print("No existen numeros multiplos de 2 en el arreglo")
else:
    print(f"El maximo multiplo de 2 es {max_mult2}")
    print(f"La posicion/es de el/los multiplos de 2 es:")
    for i in range(len(max_pos)):
            print(max_pos[i], end= " ")
for i in range(len(arreglo)):
    if min_imp == 0 and arreglo[i]%2 == 1:
        min_imp = arreglo[i]
        min_pos.append(i)
    elif arreglo[i]%2 == 1 and arreglo[i] < min_imp:
        min_imp = arreglo[i]
        min_pos = []
        min_pos.append(i)
    elif arreglo[i]%2 == 1 and arreglo[i] == min_imp:
        min_pos.append(i)
if min_imp == 0:
    print("\nNo existen numeros impares en el arreglo", end= "\n")
else:
    print(f"\nEl minimo impar es {min_imp}")
    print(f"La posicion/es de el/los minimos impares es:")
    for i in range(len(min_pos)):
            print(min_pos[i], end= " ")
arreglo.reverse()
j = -1
for i in range((len(arreglo)//2)):
    if (arreglo[i] + arreglo[j]) / 2 > 5:
        arreglo[i] = 0
        arreglo[j] = 0
    j -= 1
print("\nEl arreglo final finaliza en: ", end= "\n")
for i in range(len(arreglo)):
            print(arreglo[i], end= " ")
