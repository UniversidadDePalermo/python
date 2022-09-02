edad = int(input('Ingrese edad: '))
sexo = input('Ingrese sexo (h: Hombre, m: Mujer): ')
ocupacion = input('Ingrese ocupación (deportista/politico/actor): ')

if edad >= 90 and sexo == 'm' and ocupacion == 'actor':
  print('Mirtha Legrand')
elif edad >= 50 and sexo == 'h' and ocupacion == 'politico':
  print('Mauricio Macri')
elif edad >= 30 and sexo == 'h' and ocupacion == 'deportista':
  print('Lionel Messi')
else:
  print('No se encuentran coincidencias')
