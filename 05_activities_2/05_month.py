mes = int(input("Ingrese el numero del mes: "))

while mes > 0 and mes < 13:
    while mes %2 == 0 and mes != 2:
        print("El mes tiene 30 dias")
        mes = int(input("Ingrese el numero del mes: "))
        if mes > 12 or mes < 1:
            print("Ingrese un numero entre 1 y 12")
            mes = int(input("Ingrese el numero del mes: "))
    while mes %2 == 1:
        print("El mes tiene 31 dias")
        mes = int(input("Ingrese el numero del mes: "))
        if mes > 12 or mes < 1:
            print("Ingrese un numero entre 1 y 12")
            mes = int(input("Ingrese el numero del mes: "))
    while mes == 2:
        print("El mes tiene 28 dias")
        mes = int(input("Ingrese el numero del mes: "))
        if mes > 12 or mes < 1:
            print("Ingrese un numero entre 1 y 12")
            mes = int(input("Ingrese el numero del mes: "))
