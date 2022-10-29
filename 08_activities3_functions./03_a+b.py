def cantidad_15():
    elementos = int(input("Ingresar la cantidad de elementos que contendran ambos arreglos (menor a 15): "))
    while elementos >= 15:
        elementos = int(input("ERROR: Debe ingresar una cantidad de elementos menores a 15 que contendran ambos arreglos. Intentelo nuevamente: "))
    return elementos

def ingresar(arreglo, cantidad):
    for i in range(cantidad):
        numero = int(input("Ingrese un numero para el arreglo: "))
        arreglo.append(numero)

def mostrar(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i], end = " ")

a = []
b = []
c = []

cantidad = cantidad_15()
print("Arreglo A:")
ingresar(a, cantidad)
print("Arreglo B:")
ingresar(b, cantidad)

c = a+b

print("El arreglo C terminado es:")
mostrar(c)
