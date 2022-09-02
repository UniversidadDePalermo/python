# Valor en Km de una milla
MILLA_KM = 1.60935

# Valor en CM de una pulgada
PULGADA_CM = 2.534

unidad_a_convertir = input('Ingrese unidad a convertir.\nUse m para "milla a km" ó p para "pulgada a cm": ')

if unidad_a_convertir == "m":
  millas = input('Ingrese longitud en millas: ')
  total = float(millas) * MILLA_KM
  print(f'{float(millas)} mi = {total} km')
elif unidad_a_convertir == "p":
  pulgadas = input('Ingrese longitud en pulgadas: ')
  total = float(pulgadas) * PULGADA_CM
  print(f'{float(pulgadas)}″ = {total} cm')
else:
  print(f'La opción "{unidad_a_convertir}" no es valida. Debes ingresar "m" o "p"')
