OPC_FACTORIAL = 1
OPC_ELEVAR_POTENCIA = 2
OPC_NATURALEZA_NUMERO = 3

mensaje = 'Ingrese un número entero positivo: '
numero = int(input(mensaje))
iteracion = 1

while numero >= 0 or iteracion <= 100:
  print(f'{OPC_FACTORIAL} = Calcular el factorial para "{numero}"')
  print(f'{OPC_ELEVAR_POTENCIA} = Elevar "{numero}" a una potencia')
  print(f'{OPC_NATURALEZA_NUMERO} = Determina naturaleza del número (par, impar o nulo)')
  operacion = int(input('Opción: '))

  while operacion < OPC_FACTORIAL or operacion > OPC_NATURALEZA_NUMERO:
    print(f'La operacion "{operacion}", no es válida\n')
    print(f'{OPC_FACTORIAL} = Calcular el factorial para "{numero}"')
    print(f'{OPC_ELEVAR_POTENCIA} = Elevar "{numero}" a una potencia')
    print(f'{OPC_NATURALEZA_NUMERO} = Determina naturaleza del número (par, impar o nulo)')
    operacion = int(input('Opción: '))

  if operacion == OPC_FACTORIAL:
    factorial = 1

    if numero > 0:
      for subsiguiente in range(1, numero + 1):
        factorial = factorial * subsiguiente

      print(f'El factorial para {numero} es {factorial}')
    elif numero == 0:
      print(f'El factorial para {numero} es {factorial}')
    else:
      print(f'Los numeros negativos como {numero} no tienen valores factoriales')
  elif operacion == OPC_ELEVAR_POTENCIA:
    exponente = int(input('Ingrese exponente para elevar: '))

    print(f'{numero}^{exponente} = {numero ** exponente}')
  elif operacion == OPC_NATURALEZA_NUMERO:
    if numero == 0:
      print(f'El numero {numero} es nulo')
    elif numero % 2 == 0:
      print(f'El numero {numero} es par')
    else:
      print(f'El numero {numero} es impar')

  iteracion = iteracion + 1
  numero = int(input(mensaje))
