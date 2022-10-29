a = []
b = []
for i in range(1, 5):
    if i%2 == 1:
        i = int(input("Ingrese un valor negativo"))
        while i >= 0:
            print("Error: Debe ingresar un numero negativo. Vuelva a intentarlo.")
            i = int(input("Ingrese un valor negativo"))
        a.append(i)
    elif i%2 == 0:
        i = int(input("Ingrese un valor positivo"))
        while i <= 0:
            print("Error: Debe ingresar un numero positivo. Vuelva a intentarlo.")
            i = int(input("Ingrese un valor positivo"))
        a.append(i)
a.reverse()
print(a)
for i in range(len(a)):
    if a[i] < 0:
        b.append(a[i])
        b[i] = b[i] * (-1)
    elif a[i]%2 == 0:
        b.append(a[i])
        b[i] = b[i] //2
print(b)
a.sort()
print(a)
for i in range(len(a)-1, -1, -1):
    if a[i]%4 == 0:
        a.pop(i)
print(a)
