ganancia_anual = float(input('Ingrese el valor de la ganancia anual: '))

if ganancia_anual <= 10000:
  print('Retención: 0')
elif ganancia_anual > 10000 and ganancia_anual <= 15000:
  print(f'Retención: {(ganancia_anual - 10000) * 0.80}')
else:
  print(f'Retención: {300 + ((ganancia_anual - 15000) * 0.50)}')
