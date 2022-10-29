for iteracion in range(1, 11):
  numero = int(input('Ingrese un número del 3 al 8 no inclusive: '))

  if numero <= 3 or numero >= 8:
    print('todo mal')
  else:
    if numero == 4:
      print('Ingresaste el número 4 - Cuatro')
    elif numero == 5:
      print('Ingresaste el número 5 - Cinco')
    elif numero == 6:
      print('Ingresaste el número 6 - Seis')
    else:
      print('Ingresaste el número 7 - Siete')
