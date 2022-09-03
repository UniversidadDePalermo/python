inicio = int(input('Ingrese un numero: '))
fin = int(input('Ingrese un segundo numero: '))

if inicio < fin:
  contador = inicio + 1
  acc = 0

  while contador < fin:
    acc = acc + contador
    contador = contador + 1

  print(f'La suma es: {acc}')
else:
  print('El valor del incio debe ser menor al valor del fin')