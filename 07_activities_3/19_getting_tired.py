a = []
b = []
tot_a = 0
cant_a = 0
for i in range(15):
    i = int(input("Ingrese un numero. Si es par, se guardara en el arreglo: "))
    if i%2 == 0:
        a.append(i)
        tot_a += i
        cant_a += 1
print(a)
prom_a = tot_a // cant_a
for i in range(len(a)):
    if a[i] < prom_a:
        b.append(a[i])
print(b)
