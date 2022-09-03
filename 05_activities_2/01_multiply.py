debe_preguntar = True

while debe_preguntar:
  numero = int(input('Ingrese un numero: '))

  if numero % 3 == 0:
    debe_preguntar = False
    print(f'{numero} es multiplo de 3')
  else:
    print(f'{numero} no es multiplo de 3')
