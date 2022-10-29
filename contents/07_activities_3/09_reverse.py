a = []
n = int(input('Ingrese el numero de elementos: '))
for i in range (0, n):
    a.append(int(input("Ingrese elelemento: ")))
b = []
b = a
b = b[::-1]
print(a,b)
c = 0
for i in range(0, len(a)):
    if(a[i] == b[i]):
        c += 1
print(c)
if c == len(a):
    print("el arreglo es capicua")
else:
    print("El arreglo no es capicua")
#EL EJERCICIO FUE HECHO PARA PODER HACERSE CON DIFERENTES VALORES DE N (NO LOS16 COMO EL ENUNCIADO). SI DESEA CAMBIARLO, ELIMINE LA LINEA 2 Y REEMPLACE N POR 16 EN LA 3RA LINEA#
#No ME FUNCA .REVERSE, ME CAGO EN 10#
