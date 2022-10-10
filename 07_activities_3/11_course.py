a = []
for i in range (3):
    a.append(int(input("Ingrese el elemento: ")))
b = []
for i in range (3):
    b.append(int(input("Ingrese el elemento: ")))
max_a = 0
max_b = 0
loc_a = 0
loc_b = 0
n = 0
for i in a:
    if max_a == 0:
        max_a = i
        loc_a = n
    elif max_a < i:
        max_a = i
        loc_a = n
    n += 1
n = 0
for i in b:
    if max_b == 0:
        max_b = i
        loc_b = n
    elif max_b < i:
        max_b = i
        loc_b = n
    n += 1
print(f"El alumno mas alto del curso a es el de la posicion {loc_a} con {max_a} centimetros")
print(f"El alumno mas alto del curso a es el de la posicion {loc_b} con {max_b} centimetros")
if max_a > max_b:
    print("El curso a tiene el alumno mas alto")
elif max_a < max_b:
    print("El curso b tiene el alumno mas alto")
elif max_a == max_b:
    print("Ambos cursos tienen al menos un alumno con la misma maxima estatura. Loquisimo.")
