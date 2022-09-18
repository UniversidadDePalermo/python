mensaje_codigos_de_articulo = 'Códigos válidos: 1, 3, 5 y 7'

print(mensaje_codigos_de_articulo)
codigo_de_articulo = int(input('Ingrese código de articulo: '))

total_general_facturado = 0
cantidad_articulo_1 = 0
cantidad_articulo_3 = 0
cantidad_articulo_5 = 0
cantidad_articulo_7 = 0

while codigo_de_articulo == 1 or codigo_de_articulo == 3 or codigo_de_articulo == 5 or codigo_de_articulo == 7:
  numero_de_factura = int(input('Ingrese número de factura: '))
  cantidad_del_articulo = int(input('Ingrese cantidad del articulo: '))
  precio_unitario = int(input('Ingrese precio unitario: '))
  total_factura = cantidad_del_articulo * precio_unitario
  total_general_facturado = total_general_facturado + total_factura

  if codigo_de_articulo == 1:
    cantidad_articulo_1 = cantidad_articulo_1 + cantidad_del_articulo

  if codigo_de_articulo == 3:
    cantidad_articulo_3 = cantidad_articulo_3 + cantidad_del_articulo

  if codigo_de_articulo == 5:
    cantidad_articulo_5 = cantidad_articulo_5 + cantidad_del_articulo

  if codigo_de_articulo == 7:
    cantidad_articulo_7 = cantidad_articulo_7 + cantidad_del_articulo

  print(f'Total: $ {total_factura}')
  codigo_de_articulo = int(input('Ingrese código de articulo: '))

print(f'Total general: $ {total_general_facturado}')
print(f'Total articulo 1:  {cantidad_articulo_1}')
print(f'Total articulo 3:  {cantidad_articulo_3}')
print(f'Total articulo 5:  {cantidad_articulo_5}')
print(f'Total articulo 7:  {cantidad_articulo_7}')
