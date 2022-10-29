#Ejercicio 17#
angulo1grado = int(input("Ingresar grados del 1er Angulo: "))
angulo1minutos = int(input("Ingresar minutos del 1er Angulo: "))
angulo1segundos = int(input("Ingresar segundos del 1er Angulo: "))
angulo2grado = int(input("Ingresar grados del 2do Angulo: "))
angulo2minutos = int(input("Ingresar minutos del 2do Angulo: "))
angulo2segundos = int(input("Ingresar segundos del 2do Angulo: "))

Suma1 = angulo1segundos + angulo2segundos
Suma2 = angulo1minutos + angulo2minutos
Suma3 = angulo1grado + angulo2grado

if Suma1 >= 60:
    Suma2 += 1
    Suma1 -= 60
if Suma2 >= 60:
    Suma3 += 1
    Suma2 -= 60
print(f"La suma da como resultado {Suma3} grados, {Suma2} minutos, y {Suma1} segundos")