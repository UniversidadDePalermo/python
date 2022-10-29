"""
Una encuestadora necesita obtener aleunas estadisticas sobre el Previaje.
Para ello se le Pide a cada persona los siguientes datos:

• Nombre y apellido
• Edad
• Monto total a gastar en las vacaciones
La carga de datos finaliza cuando el nombre y apellido de la persona es "X" y la
edad y el monto total es cero.

El Previaje otorga a cada persona un credito del 50% sobre el monto total a
gastar en las vacaciones con un tope
máximo de $100,000.

Calcular y mostar.
a) El crédito que recibe cada persona por el Previaje.
b) La cantidad de personas que reciben un crédito de $100.000.
c) El nombre y apellido y la edad de la persona que recibió el menor crédito del Previaje.
d) El porcentaje de personas que gastan más de $200.000 en sus vacaciones.
e) Promedio de edad de las personas que en sus vacaciones gastan menos de $150,000.
"""

nombres = input('Ingrese nombre y apellido: ')
edad = int(input('Ingrese edad: '))
while edad < 0:
    edad = int(input('Ingrese edad: '))

gastos = int(input('Ingrese gastos: '))
while gastos < 0:
    gastos = int(input('Ingrese gastos: '))

personas_que_reciben_creditos_de_cien = 0

# el menor credito
em_nombre = nombres
em_edad = edad
em_gastos = gastos
em_credito_neto = em_gastos / 2

# d) El porcentaje de personas que gastan más de $200.000 en sus vacaciones
total_personas = 0
total_personas_con_mas_de_200k = 0
porcentaje_200k = 0

# e) Promedio de edad de las personas que en sus vacaciones gastan menos de $150,000.
# total personas que gastas menos de 150k / total suma de edades
total_suma_edades_que_gastan_menos_de_150k = 0
total_personas_que_gastan_menos_150k = 0

while nombres.upper() != 'X' and edad != 0 and gastos != 0:
    credito_neto = gastos / 2
    plata_dispoble = credito_neto + gastos

    # a) El crédito que recibe cada persona por el Previaje.
    print(f'Crédito a recibir: {credito_neto}')
    
    # b) La cantidad de personas que reciben un crédito de $100.000.
    if credito_neto == 100000:
        personas_que_reciben_creditos_de_cien += 1

    # c) El nombre y apellido y la edad de la persona que recibió el menor crédito del Previaje.
    if credito_neto < em_credito_neto:
        em_nombre = nombres
        em_edad = edad
        em_gastos = gastos
        em_credito_neto = credito_neto
        
    # d) El porcentaje de personas que gastan más de $200.000 en sus vacaciones.
    if plata_dispoble > 200000:
        total_personas_con_mas_de_200k += 1

    total_personas += 1
    porcentaje_200k = (total_personas_con_mas_de_200k / total_personas) * 100

    nombres = input('Ingrese nombre y apellido: ')
    edad = int(input('Ingrese edad: '))
    while edad < 0:
        edad = int(input('Ingrese edad: '))

    gastos = int(input('Ingrese gastos: '))
    while gastos < 0:
        gastos = int(input('Ingrese gastos: '))

if total_personas > 0:
    # b) La cantidad de personas que reciben un crédito de $100.000.
    print(f'Cantidad de personas que reciben un crédito de $100.000: {personas_que_reciben_creditos_de_cien}')

    # c) El nombre y apellido y la edad de la persona que recibió el menor crédito del Previaje.
    print(f'Persona con menor credito: {em_credito_neto}')
    print(f'Nombre: {em_nombre}')
    print(f'Edad: {em_edad}')

    # d) El porcentaje de personas que gastan más de $200.000 en sus vacaciones.
    print(f'El porcentaje total de personas que gastaron más de 200.000 es de {porcentaje_200k}')

    # e) Promedio de edad de las personas que en sus vacaciones gastan menos de $150,000.
    if total_personas_que_gastan_menos_150k > 0:
        edad_promedio = total_suma_edades_que_gastan_menos_de_150k / total_personas_que_gastan_menos_150k
        print(f'El promedio de edad de las personas que en sus vacaciones gastan menos de $150.000 es {edad_promedio}')
    else:
        print('No hay personas que gasten menos de $150.000')
