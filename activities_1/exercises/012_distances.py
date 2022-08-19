kilometraje_inicial = float(input('Ingrese kilometraje inicial: '))
kilometraje_actual = float(input('Ingrese kilometraje actual: '))
kilometros_recorridos = kilometraje_actual - kilometraje_inicial

if kilometros_recorridos < 0:
  print('El kilometraje inicial no puede ser menor al kilometraje actual')
elif kilometros_recorridos <= 100:
  print('Paciencia, falta mucho')
elif kilometros_recorridos > 100 and kilometros_recorridos <= 200:
  print('Parar para desayunar')
else:
  print('Se recomienda cargar combustible')
