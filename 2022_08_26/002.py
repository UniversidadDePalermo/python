LOCAL = 1
INTERURBANA = 2
INTERNACIONAL = 3

PRECIO_LOCAL = 0.25
PRECIO_INTERURBANA = 0.40
PRECIO_INTERNACIONAL = 1.05

print('Códigos para tipos de llamada: ')
print(f'Llamada Local: {LOCAL} ({PRECIO_LOCAL}/min)')
print(f'Llamada Interurbana: {INTERURBANA} ({PRECIO_INTERURBANA}/min)')
print(f'Llamada Internacional: {INTERNACIONAL} ({PRECIO_INTERNACIONAL}/min)')

tipo_de_llamada = int(input('Ingresa el tipo de llamada: '))

if tipo_de_llamada is not LOCAL and tipo_de_llamada is not INTERURBANA and tipo_de_llamada is not INTERNACIONAL:
  # Si el tipo de llamada no es valido, aborta la aplicación antes de proceder
  print(f'El código de llamada ingresado "{tipo_de_llamada}", no es valido')
else:
  minutos_duracion = int(input('Ingresa la duracion en minutos: '))

  if tipo_de_llamada == LOCAL:
    print(f'Debe pagar {minutos_duracion * PRECIO_LOCAL} AR$ por {minutos_duracion:.0f} minutos')
  elif tipo_de_llamada == INTERURBANA:
    print(f'Debe pagar {minutos_duracion * PRECIO_INTERURBANA} AR$ por {minutos_duracion:.0f} minutos')
  elif tipo_de_llamada == INTERNACIONAL:
    print(f'Debe pagar {minutos_duracion * PRECIO_INTERNACIONAL} AR$ por {minutos_duracion:.0f} minutos')
