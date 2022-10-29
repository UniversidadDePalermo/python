"""
Leer un número y calcular la suma de los números naturales hasta ese número.
Modificar el algoritmo para que se pueda procesar muchos números. #
Dar por terminada la entrada cuandoel número sea 0.
"""

numero = int(input('Ingrese un numero natural: '))
while numero < 0:
  numero = int(input('Ingrese un numero natural: '))

# Dar por terminada la entrada cuandoel número sea 0.
while numero != 0:
  valor = 0

  while numero > 0:
    valor += numero
    numero -= 1

  print(f'Resultado: {valor}')

  # Volver a preguntar
  numero = int(input('Ingrese un numero natural: '))
  while numero < 0:
    numero = int(input('Ingrese un numero natural: '))
