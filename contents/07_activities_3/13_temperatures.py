temperatura = []
volumen = []
n = int(input("Cuantos datos desea ingresar de temperatura y volumen?: "))
for i in range(0, n):
    temperatura.append(int(input("Ingrese valor de temperatura: ")))
    volumen.append(int(input("Ingrese valor de volumen: ")))
temp_max = temperatura[0]
pos_max = 0
temp_min = temperatura[0]
pos_min = 0
for i in range(0, n):
    if temperatura[i] > temp_max:
        temp_max = temperatura[i]
        pos_max = i
    if temperatura[i] < temp_min:
        temp_min = temperatura[i]
        pos_min = i
print(f"Se registro una temperatura maxima de {temp_max} grados con un volumen de {volumen[pos_max]} cm3 y una temperatura minima de {temp_min} grados con un volumen de {volumen[pos_min]} cm3")
temperatura.sort()
print("Temperaturas: ")
for i in range(len(temperatura)):
    print(temperatura[i], end=" ")
