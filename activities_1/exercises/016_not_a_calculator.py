numero_a = int(input('Ingrese un número entero: '))
numero_b = int(input('Ingrese un segundo número entero: '))

if (numero_a < 0 and numero_b > 0) or (numero_a > 0 and numero_b < 0):
  print('Producto será negativo')
elif (numero_a > 0 and numero_b > 0) or (numero_a < 0 and numero_b < 0):
  print('Producto será positivo')
elif numero_a == 0 or numero_b == 0:
  print('Producto será 0')
