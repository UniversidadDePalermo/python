total_num_positivo = 0

mensaje = 'Ingrese un número [0 para finalizar]: '
numero = int(input(mensaje))
while numero > 0:
  numero = int(input(mensaje))

  if numero > 0:
    total_num_positivo += 1

print(f'Total números positivos: {total_num_positivo}')
