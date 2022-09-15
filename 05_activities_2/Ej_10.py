"""
Se realiza un censo en la provincia de Buenos Aires.

Por cada persona censada se ingresa:
  - Sexo(1.F, 2.M)
  - Edad
  - Estudios Cursados:
    - 1 para estudios primarios
    - 2 paraestudios secundarios
    - 3 para estudios terciarios

  Diseñar un programa que permita ingresar los datos y calcular:
    a. Cantidad de hombres mayores a 45 años
    b. Cantidad de mujeres encuestadas
    c. Promedio de edad de las personas para cada tipo de estudio
    d. Porcentaje de mujeres con estudios terciarios
    e. Porcentaje de hombres mayores a 30 años con estudios terciarios
    f. Promedio de edad de las mujeres mayores a 40 años con estudios
      secundarios

La carga de datos finaliza cuando ingresa 0 en edad y en estudios cursados.
"""
SEXO_FEMENINO = 1
SEXO_MASCULINO = 2

#contadores
hombres_M45 = 0 #hombres mayores a 45
mujeres_encuestadas = 0 #mujeres encuestadas

edad_total = 0 
total_encuestados = 0 #total de encuestados
mujeres_terceario = 0 #total mujeres terceario
hombres_tercearioM30 = 0 #mayores a 30
mujeres_secundarioM40 = 0

# Cantidades de personas que estudian niveles de educación
primaria_cont = 0
secundaria_cont = 0
terciario_cont = 0

# Acumulado de edades por nivel de educación
primaria_edad_acum = 0
secundaria_edad_acum = 0
terciario_edad_acum = 0

# Start: Tomo valores del primer ciudadano
sexo = int(input("Ingrese sexo: \n1.F \n2.M\nRespuesta: "))
while sexo < SEXO_FEMENINO or sexo > SEXO_MASCULINO:
  sexo = int(input("Ingrese sexo: \n1.F \n2.M\nRespuesta: "))

edad = int(input("Ingrese edad: "))
while edad < 0:
  edad = int(input("Ingrese edad: "))

estudios = int(input("Ingrese estudios cursados: "))
while estudios < 0 or estudios > 3:
  edad = int(input("Ingrese estudios cursados: "))
# End: Tomo valores del primer ciudadano


# Start: Calculo de datos y contadores
while edad != 0 and estudios != 0:
  if sexo == SEXO_MASCULINO and edad >= 45:
    # a. Cantidad de hombres mayores a 45 años
    hombres_M45 += 1

  if sexo == SEXO_FEMENINO:
    # b. Cantidad de mujeres encuestadas
    mujeres_encuestadas +=1 

  # Sumadores de nivel de estudios
  if estudios == 1:
    primaria_cont += 1
    primaria_edad_acum += edad
  elif estudios == 2:
    secundaria_cont +=1
    secundaria_edad_acum += edad

    if sexo == SEXO_FEMENINO and edad > 40:
      # f. Promedio de edad de las mujeres mayores a 40 años con estudios
      # secundarios
      mujeres_secundarioM40 += 1

  elif estudios == 3:
    terciario_cont +=1
    terciario_edad_acum += edad

    if sexo == SEXO_FEMENINO:
      # d. Porcentaje de mujeres con estudios terciarios
      mujeres_terceario += 1

    if sexo == SEXO_MASCULINO and edad > 30:
      # e. Porcentaje de hombres mayores a 30 años con estudios terciarios
      hombres_tercearioM30 += 1

  sexo = int(input("Ingrese sexo: \n1.F \n2.M\nRespuesta: "))
  while sexo < 1 or sexo > 2:
    sexo = int(input("Ingrese sexo: \n1.F \n2.M\nRespuesta: "))

  edad = int(input("Ingrese edad: "))
  while edad < 0:
    edad = int(input("Ingrese edad: "))

  estudios = int(input("Ingrese estudios cursados: "))
  while estudios < 0 or estudios > 3:
    edad = int(input("Ingrese estudios cursados: "))

  total_encuestados += 1
# End: Calculo de datos y contadores

if total_encuestados == 0:
    print("No hay datos")
else:
    print(f"La cantidad de hombres mayores a 45 encuestados es {hombres_M45}")
    print(f"La cantidad de mujeres encuestadas es de {mujeres_encuestadas}")

    # c. Promedio de edad de las personas para cada tipo de estudio
    if primaria_cont != 0:
      print(f'El promedio de edad de personas con nivel de educación primario es de {primaria_edad_acum / primaria_cont}')

    if secundaria_cont != 0:
      print(f'El promedio de edad de personas con nivel de educación secundario es de {secundaria_edad_acum / secundaria_cont}')

    if terciario_cont != 0:
      print(f'El promedio de edad de personas con nivel de educación terciario es de {terciario_edad_acum / terciario_cont}')
