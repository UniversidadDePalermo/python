# Dado un arreglo de n elementos, calcular e imprimir el menor de los múltiplos de 5 y el mayor de los múltiplos de 10. Determinar la posición de cada uno de ellos

arreglo = []

n = int(input("Ingrese la cantidad de posiciones del arreglo: "))
for i in range(0, n): 
    i = int(input("Ingrese un elemeto del arreglo: "))
    arreglo.append(i)

# menor de los multiplos de 5
i = 0
while i < len(arreglo) and arreglo[i] % 5 != 0: 
   i += 1

if i != len(arreglo): 
    min_5 = arreglo[i] 
    min_pos_5 = i 
    for p in range(i, len(arreglo)): 
        if min_5 > arreglo[p] and arreglo[p] % 5 == 0: 
            min_5 = arreglo[p] 
            min_pos_5 = p 
    print(f"La posición que ocupa el mínimo valor de los multiplos de 5 es {min_pos_5+1} y su valor es {min_5} ")
else: 
    print("No hay multiplos de 5 en el arreglo") 


# mayor de los múltiplos de 10
i = 0 
while i < len(arreglo) and arreglo[i] % 10 != 0: 
   i += 1 

if i != len(arreglo):
    max_10 = arreglo[i] 
    max_pos_10 = i 
    for p in range(i, len(arreglo)): 
        if max_10 < arreglo[p] and arreglo[p] % 10 == 0:
            max_10 = arreglo[p] 
            max_pos_10 = p 
    print(f"La posición que ocupa el maximo valor de los multiplos de 10 es {max_pos_10+1} y su valor es {max_10} ")
else: 
    print("No hay multiplos de 10 en el arreglo") 
