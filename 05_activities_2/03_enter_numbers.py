debe_preguntar = True
total_num_positivo = 0

while debe_preguntar:
  numero = int(input('Ingrese un número: '))

  if numero == 0:
    debe_preguntar = False
  elif numero > 0:
    total_num_positivo += 1

print(f'Total números positivos: {total_num_positivo}')
