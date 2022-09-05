numero = input('Ingrese un número mayor o igual a 100: ')
numero = int(numero)

if numero < 100 or numero > 999:
  print('El numero ingresado no es valido.')
  print('Debe de ingresar un número mayor o igual a 100.')
else:
  primer_digito = numero % 10
  segundo_digito = int((numero / 10) % 10)
  tercer_digito = int((numero / 100) % 10)

  print(f'El segundo dígito es: {segundo_digito}')
