edad_min = 10000
edad_max = 0

for x in range(50):
    edad = int(input("Ingresar la edad: "))
    while edad < 0 or edad > 140:
        print("Error: Esa edad es imposible!")
        edad = int(input("Ingresar la edad: "))
    if edad > edad_max:
        edad_max = edad
    if edad < edad_min:
        edad_min = edad
print(f"El rango de edades oscila entre {edad_min} y {edad_max} años")
