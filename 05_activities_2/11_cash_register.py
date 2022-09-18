mensaje_codigos_de_articulo = 'Códigos válidos: 1, 3, 5 y 7'

print(mensaje_codigos_de_articulo)
codigo_de_articulo = int(input('Ingrese código de articulo: '))

total_general_facturado = 0

cantidad_articulo_1 = 0
cantidad_articulo_3 = 0
cantidad_articulo_5 = 0
cantidad_articulo_7 = 0

facturas_articulo_1 = 0
facturas_articulo_3 = 0
facturas_articulo_5 = 0
facturas_articulo_7 = 0

numero_de_factura_mayor_valor = 0
valor_de_factura_mayor_valor = 0

while codigo_de_articulo == 1 or codigo_de_articulo == 3 or codigo_de_articulo == 5 or codigo_de_articulo == 7:
  numero_de_factura = int(input('Ingrese número de factura: '))
  cantidad_del_articulo = int(input('Ingrese cantidad del articulo: '))

  while cantidad_del_articulo <= 0:
    print('La cantidad del articulo debe ser mayor o igual a 1')
    cantidad_del_articulo = int(input('Ingrese cantidad del articulo: '))

  precio_unitario = int(input('Ingrese precio unitario: '))

  while precio_unitario < 0:
    print('El precio unitario debe ser mayor o igual a 0')
    precio_unitario = int(input('Ingrese precio unitario: '))

  total_factura = cantidad_del_articulo * precio_unitario
  total_general_facturado = total_general_facturado + total_factura

  if codigo_de_articulo == 1:
    cantidad_articulo_1 = cantidad_articulo_1 + cantidad_del_articulo
    facturas_articulo_1 += 1

  if codigo_de_articulo == 3:
    cantidad_articulo_3 = cantidad_articulo_3 + cantidad_del_articulo
    facturas_articulo_3 += 1

  if codigo_de_articulo == 5:
    cantidad_articulo_5 = cantidad_articulo_5 + cantidad_del_articulo
    facturas_articulo_5 += 1

  if codigo_de_articulo == 7:
    cantidad_articulo_7 = cantidad_articulo_7 + cantidad_del_articulo
    facturas_articulo_7 += 1

  # a. Total de cada factura
  print(f'Total: $ {total_factura}')

  # f. Nro. de factura con mayor valor (en $)
  if total_factura > valor_de_factura_mayor_valor:
    valor_de_factura_mayor_valor = total_factura
    numero_de_factura_mayor_valor = numero_de_factura

  codigo_de_articulo = int(input('Ingrese código de articulo: '))

# b. Total general facturado
print(f'Total general: $ {total_general_facturado}')

# c. Cantidad vendida (en unidades) para cada uno de los artículos.
print(f'Total articulo 1:  {cantidad_articulo_1}')
print(f'Total articulo 3:  {cantidad_articulo_3}')
print(f'Total articulo 5:  {cantidad_articulo_5}')
print(f'Total articulo 7:  {cantidad_articulo_7}')

# d. Total de artículos vendidos
print(f'Cantidad de artículos vendidos: {cantidad_articulo_1 + cantidad_articulo_3 + cantidad_articulo_5 + cantidad_articulo_7}')

# e. Cantidad de facturas emitidas para cada uno de los artículos.
print(f'Total facturas articulo 1:  {facturas_articulo_1}')
print(f'Total facturas articulo 3:  {facturas_articulo_3}')
print(f'Total facturas articulo 5:  {facturas_articulo_5}')
print(f'Total facturas articulo 7:  {facturas_articulo_7}')
