def ingresar_menos15_para2arreglos(arreglo, arreglo2):
    elementos = int(input("Ingresar la cantidad de elementos que contendran ambos arreglos (menor a 15): "))
    while elementos >= 15:
        elementos = int(input("ERROR: Debe ingresar una cantidad de elementos menores a 15 que contendran ambos arreglos. Intentelo nuevamente: "))
    for i in range(elementos):
        numero = int(input("Ingrese un numero para el primer arreglo: "))
        arreglo.append(numero)
    for i in range(elementos):
        numero = int(input("Ingrese un numero para el segundo arreglo: "))
        arreglo2.append(numero)
    return elementos
    return numero

def mostrar(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i], end = " ")

a = []
b = []
c = []

ingresar_menos15_para2arreglos(a, b)

c = a+b

print("El arreglo c terminado es:")
mostrar(c)
