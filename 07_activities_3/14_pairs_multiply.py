a = []
b = []
c = []
d = []
tot_c = 0
may_prom_c = 0

for i in range(3):
    n = (int(input("Ingrese un valor para a: ")))
    while n%2 != 0:
        print("El numero ingresado debe ser par")
        n = (int(input("Ingrese un valor para a: ")))
    a.append(n)
    n = (int(input("Ingrese un valor para b: ")))
    while n%5 != 0:
        print("El numero ingresado debe ser multiplo de 5")
        n = (int(input("Ingrese un valor para b: ")))
    b.append(n)
for i in range(0, len(a)):
    suma = a[i] + b[i]
    c.append(suma)
print(c)
d = a + b
print(d)
a.reverse()
print(a)
b_max = b[0]
b_pos = 0
for i in range(0, len(b)):
    if b[i] > b_max:
        b_max = b[i]
        b_pos = i
for i in range(b_pos+1, len(b)):
    b[i] = 0
print(f"El valor maximo de b es {b_max} en la posicion {b_pos}.")
print(b)
for i in c:
    tot_c += i
prom_c = tot_c / len(c)
for i in c:
    if i > prom_c:
        may_prom_c += 1
print(f"Existen {may_prom_c} valores mayores al promedio de c ({prom_c}).")
