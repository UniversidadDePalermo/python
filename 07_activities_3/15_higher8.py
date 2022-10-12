a = []
total_not = 0
cantidad_not = 0
for i in range(20):
    i = int(input("Ingrese el numero: "))
    if i > 20 and len(a) < 8:
        a.append(i)
    else:
        total_not += i
        cantidad_not += 1
if len(a) == 0:
    print("No hay numeros dentro de a. Saliendo del programa.")
elif len(a) < 8 or len(a) == 8:
    prom_not = total_not / cantidad_not
    print(f"El promedio de los numeros que no entraron en el calculo es de {prom_not}")
    while len(a) < 8:
        a.append(a[0])
    a_max = a[0]
    pos_ant = i
    for i in range(len(a)):
        valor = a[i]
        if valor > a_max:
            a_max = a[i]
            pos_ant = i-1
            elem_ant = a[pos_ant]
    if a_max == a[0]:
        print(f"No existe numero anterior al maximo de a ({a_max})")
    else:
        print(f"El numero mayor es {a_max} y el numero anterior es {elem_ant}")
    for i in range(len(a)):
        if i%2 == 0:
            factorial = 0
            for j in range(a[i], 0, -1):
                if factorial == 0:
                    factorial = j
                else:
                    factorial *= j
            print(f"El factorial de i es {factorial}")
