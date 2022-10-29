arreglo = []
arreglo_mayor = []

for i in range(10):
    j = int(input("Ingrese la edad del cliente: "))
    while j < 18:
        j = int(input("Ingrese la edad del cliente, para ser registrada en la lista debe ser mayor a 18 años: "))
    arreglo.append(j)
    if i == 0:
        tot_edades = j
        cliente_mas_antiguo = j
    else:
        tot_edades += j
        if j > cliente_mas_antiguo:
            cliente_mas_antiguo = j
for i in range(len(arreglo)):
    print(arreglo[i], end= " ")
promedio = tot_edades // len(arreglo)
print(f"\nEl promedio de edades de los clientes es de {promedio} años.")
print(f"El cliente mas antiguo tiene {cliente_mas_antiguo} años.")
for i in range(len(arreglo)):
    if arreglo[i] > promedio:
        arreglo_mayor.append(arreglo[i])
print("Edades mayores al promedio:")
for i in range(len(arreglo_mayor)):
    print(arreglo_mayor[i], end= " ")
for i in range(((len(arreglo_mayor)) //2), len(arreglo_mayor)):
    for j in range(((len(arreglo_mayor))//2) +1, len(arreglo_mayor)):
        if arreglo_mayor[i] > arreglo_mayor[j]:
            aux = arreglo_mayor[i]
            arreglo_mayor[i] = arreglo_mayor[j]
            arreglo_mayor[j] = aux
print("\n Arreglo de mayores al promedio con la mitad ordenada ascendentemente")
for i in range(len(arreglo_mayor)):
    print(arreglo_mayor[i], end= " ")
i = 0
while arreglo[i]%2 == 1:
    i += 1
if arreglo[i]%2 == 0:
    arreglo.pop(i)
print("\n Arreglo sin la primera edad par:")
for i in range(len(arreglo)):
    print(arreglo[i], end= " ")
