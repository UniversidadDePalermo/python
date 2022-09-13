FACTORIAL = 1
ELEVAR_POTENCIA = 2

mensaje = 'Ingrese un número entero positivo: '
numero = int(input(mensaje))
iteracion = 1

while numero >= 0 or iteracion <= 100:
  iteracion = iteracion + 1

  print(f'{FACTORIAL} = Calcular el factorial para "{numero}"')
  print(f'{ELEVAR_POTENCIA} = Elevar "{numero}" a una potencia')
  print(f'3. Determina naturaleza del número (par, impar o nulo)')
  operacion = int(input('Opción: '))

  if operacion == FACTORIAL:
    factorial = 1

    if numero > 0:
      for subsiguiente in range(1, numero + 1):
        factorial = factorial * subsiguiente

      print(f'El factorial para {numero} es {factorial}')
    elif numero == 0:
      print(f'El factorial para {numero} es {factorial}')
    else:
      print(f'Los numeros negativos como {numero} no tienen valores factoriales')
  elif operacion == ELEVAR_POTENCIA:
    exponente = int(input('Ingrese exponente para elevar: '))

    print(f'{numero}^{exponente} = {numero ** exponente}')
  else:
    if numero == 0:
      print(f'El numero {numero} es nulo')
    elif numero % 2 == 0:
      print(f'El numero {numero} es par')
    else:
      print(f'El numero {numero} es impar')

  numero = int(input(mensaje))
