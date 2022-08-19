print('Valores del primer ángulo: ')
grados_a = float(input('Ingrese grados: '))
minutos_a = int(input('Ingrese minutos: '))
segundos_a = int(input('Ingrese segundos: '))

print('\nValores del segundo ángulo: ')
grados_b = float(input('Ingrese grados: '))
minutos_b = int(input('Ingrese minutos: '))
segundos_b = int(input('Ingrese segundos: '))

excede_minutos = minutos_a > 60 or minutos_b > 60
excede_segundos = segundos_a > 60 or segundos_b > 60

if excede_minutos:
  print('Los minutos no deben excederse de 60\'')

if excede_segundos:
  print('Los segundos no deben excederse de 60\'\'')

if not excede_minutos and not excede_segundos:
  suma_grados = grados_a + grados_b
  suma_minutos = minutos_a + minutos_b
  suma_segundos = segundos_a + segundos_b

  if suma_segundos > 60:
    minutos = suma_segundos / 60
    segundos = minutos - int(minutos)
    suma_segundos = segundos * 60
    suma_minutos = minutos + suma_minutos

  if suma_minutos > 60:
    grados = suma_minutos / 60
    minutos = grados - int(grados)
    suma_minutos = minutos * 60
    suma_grados = minutos + suma_grados

  print(f'{int(suma_grados)}º {int(suma_minutos)}\'\' {int(suma_segundos)}\'')
