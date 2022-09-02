dividendo = float(input('Ingrese un numero: '))
divisor = float(input('Ingrese un segundo numero: '))

if dividendo != 0 and divisor != 0:
  cociente = dividendo / divisor
  print(f'El cociente de {dividendo} / {divisor} = {cociente}')
else:
  print('No se puede realizar el cociente')
