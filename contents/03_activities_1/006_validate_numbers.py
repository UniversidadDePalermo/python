from math import sqrt

numero = input('Ingrese un número: ')
numero = float(numero)

if numero > 0:
  raiz_cuadrada = sqrt(numero)
  print(f'La raiz cuadrada de {numero} es {raiz_cuadrada}')
elif numero < 0:
  cuadrado = numero ** 2
  print(f'El cuadrado de {numero} es {cuadrado}')
else:
  print('Error. Ha ingresado un valor nulo')
