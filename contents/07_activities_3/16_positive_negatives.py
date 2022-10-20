a = []
multiplos_4 = []
tot_neg = 0
cant_neg = 0
pares = 0
multiplos_3 = 0
for i in range(10):
    i = int(input("Ingrese el numero a agregar a la lista. Deberan ser 5 positivos y 5 negativos, en ese orden: "))
    if len(a) < 5:
        while i <= 0:
            print("Dato erroneo: ingrese un numero mayor a 0")
            i = int(input("Ingrese el numero a agregar a la lista. Deberan ser 5 positivos y 5 negativos, en ese orden: "))
        a.append(i)
    elif len(a) >= 5:
        while i >= 0:
            print("Dato erroneo: ingrese un numero menor a 0")
            i = int(input("Ingrese el numero a agregar a la lista. Deberan ser 5 positivos y 5 negativos, en ese orden: "))
        a.append(i)
        print(a)
for i in range(5, len(a)):
    tot_neg += a[i]
    cant_neg += 1
prom_neg = tot_neg / cant_neg
print(f"El promedio de los numeros negativos es de {prom_neg}")
a.sort()
print(a)
for i in range(len(a)):
    if i%4 == 0:
        multiplos_4.append(i)
if len(multiplos_4) == 0:
    print("El arreglo de multiplos de 4 no contiene elementos")
else:
    print("El arreglo de multiplos de 4 contiene elementos")
    for i in range(len(multiplos_4)):
        if multiplos_4[i]%2 == 0:
            pares += 1
        if multiplos_4[i]%3 == 0:
            multiplos_3 += 1
    print(f"El arreglo de multiplos de 4 tiene {pares} numeros pares")
    print(f"El arreglo de multiplos de 4 tiene {multiplos_3} numeros multiplos de 3")
