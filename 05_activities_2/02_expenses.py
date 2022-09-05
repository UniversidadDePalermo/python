numero_semana = 1
gastos_totales = 0

while numero_semana <= 5:
  gastos = int(input(f'Ingrese gastos de semana {numero_semana}: '))
  gastos_totales += gastos
  numero_semana += 1

promedio = int(gastos_totales / 5)
print(f'Promedio de gastos: ${promedio}')
