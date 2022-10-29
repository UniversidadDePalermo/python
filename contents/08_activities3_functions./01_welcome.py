def ingresar(arreglo):
    for i in range(3):
        numero = int(input("Ingrese un numero: "))
        arreglo.append(numero)

def mostrar(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i], end = " ")


a = []

ingresar(a)
print(f"El numero de componentes del arreglo es de {len(a)}")
mostrar(a)
