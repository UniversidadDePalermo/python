#6# SIN FUNCIONES
a = []
b = []
c = []
n = int(input("Cantidad de elementos del primer arreglo: "))
for i in range(0,n):
        a.append(int(input("Ingrese un elemento de arreglo: ")))
m = int(input("Cantidad de elementod del segundo arreglo: "))
for i in range(0,m):
        b.append(int(input("Ingrese un elemento de arreglo: ")))
for i in range(0, len(a)):
        for j in range(0, len(b)):
            if(a[i]==b[j]):
                c.append(a[i])
print("Los siguientes elementos pertenecen a los dos arreglos: ")
for i in range(0, len(c)):
        print(c[i])



#6# CON FUNCIONES
def generar(arreglo, n):
    for i in range(0,n):
        arreglo.append(int(input("Ingrese un elemento de arreglo: ")))

def interseccion(arreglo1, arreglo2, comunes):
    for i in range(0, len(arreglo1)):
        for j in range(0, len(arreglo2)):
            if(arreglo1[i]==arreglo2[j]):
                comunes.append(arreglo1[i])

def mostrar(arreglo):
    for i in range(0, len(arreglo)):
        print(arreglo[i])
        
a = []
b = []
c = []
n = int(input("Cantidad de elementod del primer arreglo: "))
generar(a,n)
m = int(input("Cantidad de elementod del segundo arreglo: "))
generar(b,m)
interseccion(a,b,c)
print("Los siguientes elementos pertenecen a los dos arreglos: ")
mostrar(c)
