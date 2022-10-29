mensaje = 'Ingrese un numero: '
numero = int(input(mensaje))
while numero % 3 != 0:
  numero = int(input(mensaje))

  if numero % 3 == 0:
    print(f'{numero} es multiplo de 3')
  else:
    print(f'{numero} no es multiplo de 3')
