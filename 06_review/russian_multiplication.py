multiplicando = int(input('Ingrese el multiplicando: '))
multiplicador = int(input('Ingrese el multiplicador: '))
mostrar_tabla = input('Desea mostrar tabla [Y/N]: ')

accum = multiplicando
mitad = multiplicador
doble = multiplicando

while mitad >= 1 and multiplicador != 0 and multiplicando != 0:
  if mostrar_tabla and doble == multiplicando:
    # Muestra el encabezado de la tabla solo la primera vez
    print('Doble - Mitad')

  doble = doble * 2
  mitad = int(mitad / 2)

  if mostrar_tabla.upper() == 'Y':
    # Muestra la tabla en cada iteración si el usuario ingresa 'Y'
    # al iniciar
    print(f'{doble} - {mitad}')

  if mitad % 2 != 0:
    # Sí y solo sí mitad es impar debo sumar
    accum += doble

print(f'{multiplicando} x {multiplicador} = {accum}')
