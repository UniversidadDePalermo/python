"""Una empresa liquida sueldos según la categoría de cada empleado y paga por hora según la siguiente tabla:
 categoría 1: $150
 categoría 2: $200
 categoría 3: $250
 categoría 4: $280

Diseñar un programa que permita ingresar la categoría de cada empleado y las horas que trabajo en el mes y calcule:
a. Calcular el sueldo bruto y el sueldo neto (descontar 17% de aportes) de cada empleado
b. Calcular el total de sueldos que paga la empresa --> ACUMULADOR
c. Determinar cuántos empleados de cada categoría hay --> ACUMULADOR DE CADA CATEGORÍA """

# SUELDO BRUTO --> SIN IMPUESTOS
# SUELDO NETO --> LO QUE TE QUEDA DE TODAS LAS DEDUCCIONES

acum_total_sueldos = 0 # ACUMULADOR EN 0 DE PREG B
acum_cat1 = 0
acum_cat2 = 0
acum_cat3 = 0
acum_cat4 = 0

categoria = int(input("\nCategoría 1 = 1 \nCategoría 2 = 2 \nCategoría 3 = 3 \nCategoría 4 = 4 \nIngresar la categoría del empleado - si se ingresa 0 se cierra el programa: "))
while categoria != 0:
    while categoria < 0 and categoria > 4: #VALIDO CATEGORÍA
        print("Ingrese una categoría correcta (1-4): ")
        categoria = int(input("Ingresar la categoría del empleado - si se ingresa 0 se cierra el programa: "))

    horas = int(input("Ingrese las hs trabajadas en el mes: ")) # PREGUNTO HORAS

    while horas < 0: # VALIDO HORAS CORRECTAS
        print("Flaco no existen hs negativas")
        categoria = int(input("Ingresar la categoría del empleado - si se ingresa 0 se cierra el programa: "))

    # while categoria >= 1 and categoria <= 4: --> NO HACE FALTA :)
        # PREG A
    if categoria == 1:
        sueldo_bruto = horas*150
        sueldo_neto = sueldo_bruto - (sueldo_bruto*0.17)
        acum_cat1 = acum_cat1 + 1
        print(f"El sueldo bruto es de {sueldo_bruto} y el sueldo neto es de {sueldo_neto}") #PRINT PREG A
    elif categoria == 2:
        sueldo_bruto = horas*200
        sueldo_neto = sueldo_bruto - (sueldo_bruto*0.17)   
        acum_cat2 = acum_cat2 + 1
        print(f"El sueldo bruto es de {sueldo_bruto} y el sueldo neto es de {sueldo_neto}")        
    elif categoria == 3:
        sueldo_bruto = horas*250
        sueldo_neto = sueldo_bruto - (sueldo_bruto*0.17)
        acum_cat3 = acum_cat3 + 1     
        print(f"El sueldo bruto es de {sueldo_bruto} y el sueldo neto es de {sueldo_neto}")   
    elif categoria == 4:
        sueldo_bruto = horas*280
        sueldo_neto = sueldo_bruto - (sueldo_bruto*0.17)
        acum_cat4 = acum_cat4 + 1  
        print(f"El sueldo bruto es de {sueldo_bruto} y el sueldo neto es de {sueldo_neto}")

    
    # PREG B
    acum_total_sueldos = acum_total_sueldos + 1 # ACÁ YA CALCULO EL TOTAL DE LOS SUELDOS

    categoria = int(input("Ingresar la categoría del empleado - si se ingresa 0 se cierra el programa: "))   # vuelvo a preguntar DENTRO DEL BUCLE para volver a entrar en el bucle

    while categoria < 0 and categoria > 4: #VALIDO CATEGORÍA
        print("Ingrese una categoría correcta (1-4): ")
        categoria = int(input("Ingresar la categoría del empleado - si se ingresa 0 se cierra el programa: "))

if acum_total_sueldos == 0:
    print("Saliste del programa")
else:
    print(f"El total de sueldos que paga la empresa al mes es de {acum_total_sueldos}") #PRINT PREG B
    print(f"En la categoría 1 hay {acum_cat1} empleados, en la categoría 2 hay {acum_cat2} empleados, en la categoría 3 hay {acum_cat3} empleados y en la categoría 4 hay {acum_cat4} empleados,") #PRINT PREG C