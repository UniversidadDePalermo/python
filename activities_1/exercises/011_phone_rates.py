LOCAL = 1
INTERURBANA = 2
INTERNACIONAL = 3

PRECIO_LOCAL = 0.25
PRECIO_INTERURBANA = 0.40
PRECIO_INTERNACIONAL = 1.05

print('Códigos para tipos de llamada: ')
print(f'Llamada Local: {LOCAL}')
print(f'Llamada Interurbana: {INTERURBANA}')
print(f'Llamada Internacional: {INTERNACIONAL}')

tipo_de_llamada = int(input('Ingresa el tipo de llamada: '))
minutos_duracion = int(input('Ingresa la duracion en minutos: '))

if tipo_de_llamada == LOCAL:
  print(f'Debe pagar {minutos_duracion * PRECIO_LOCAL} AR$')
elif tipo_de_llamada == INTERURBANA:
  print(f'Debe pagar {minutos_duracion * PRECIO_INTERURBANA} AR$')
elif tipo_de_llamada == INTERNACIONAL:
  print(f'Debe pagar {minutos_duracion * PRECIO_INTERNACIONAL} AR$')
else:
  print(f'El código de llamada ingresado "{tipo_de_llamada}", no es valido')
