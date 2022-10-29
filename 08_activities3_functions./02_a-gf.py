def ingresar_10(arreglo):
    for i in range(5):
        numero = int(input("Ingrese un numero: "))
        arreglo.append(numero)

def mostrar_componente(arreglo):
    print(f"El componente a mostrar es el {arreglo}")

def inv_mos_arreglo(arreglo):
    arreglo_inv = []
    for i in range(len(arreglo)-1, -1, -1):
        arreglo_inv.append(arreglo[i])
    print(f"El arreglo invertido seria:")
    for i in range(len(arreglo_inv)):
        print(arreglo_inv[i], end = " ")
    return arreglo_inv

def producto(arreglo):
    producto = arreglo[0]*arreglo[-1]
    print(f"\nEl producto entre el primer y ultimo componente es {producto}")
    return producto

def mostrar_ind_impar(arreglo):
    print("Se imprimen los componentes de indice impar:")
    for i in range(1, len(arreglo), 2):
        print(arreglo[i], end= " ")

def suma_ind_par(arreglo):
    for i in range(0, len(arreglo), 2):
        if i == 0:
            suma = arreglo[i]
        else:
            suma += arreglo[i]
    print(f"\nLa suma de los componentes de indice par es de {suma}")
    return suma

def multiply_ind_par(arreglo):
    for i in range(1, len(arreglo), 2):
        if i == 1:
            multiply = arreglo[i]
        else:
            multiply *= arreglo[i]
    print(f"La multiplicacion de los componentes de indice impar es de {multiply}")
    return multiply

def cambiar_primer_ultimo(arreglo):
    aux = arreglo[-1]
    arreglo[-1] = arreglo[0]
    arreglo[0] = aux
    return aux

def mostrar(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i], end = " ")



a = []

ingresar_10(a)

#a#

mostrar_componente(a[3])

#b#

inv_mos_arreglo(a)

#c#

producto(a)

#d#

mostrar_ind_impar(a)

#e#

suma_ind_par(a)

#f#

multiply_ind_par(a)

#e#

cambiar_primer_ultimo(a)
mostrar(a)
