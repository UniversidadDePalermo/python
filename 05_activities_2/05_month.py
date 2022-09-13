numero_de_mes = int(input('Ingrese número de mes: '))

if numero_de_mes >= 1 and numero_de_mes <= 12:
  if numero_de_mes == 1:
    print('Enero tiene 31 días')
  elif numero_de_mes == 2:
    print('Febrero tiene 28 días')
  elif numero_de_mes == 3:
    print('Febrero tiene 28 días')
else:
  print('Esta mal')
