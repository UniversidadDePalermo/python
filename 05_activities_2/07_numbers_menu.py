numero_a = int(input('Ingrese un número: '))
numero_b = int(input('Ingrese un segundo número: '))
mensaje = 'Seleccione una opción: \n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir (Si el segundo número es cero, no se efecturá la operación.)\n5. Salir del Programa\nIngrese una opción: '
operacion = int(input(mensaje))

while operacion != 5:
  if operacion == 1:
    print(f'{numero_a} + {numero_b} = {numero_a + numero_b}')
  elif operacion == 2:
    print(f'{numero_a} - {numero_b} = {numero_a - numero_b}')
  elif operacion == 3:
    print(f'{numero_a} * {numero_b} = {numero_a * numero_b}')
  elif operacion == 4:
    if numero_b == 0:
      print('No se puede dividir entre cero')
      numero_b = int(input('Ingrese nuevo dividendo: '))

      while numero_b == 0:
        print('No se puede dividir entre cero')
        numero_b = int(input('Ingrese nuevo dividendo: '))

    print(f'{numero_a} / {numero_b} = {numero_a / numero_b}')
  else:
    print(f'La opción {operacion} no es soportada')

  operacion = int(input(mensaje))

print('Finalizo el programa')
