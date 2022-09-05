limite = int(input('Ingrese número: '))
suma = 0
resultado = ''

while suma <= limite:
  resultado += f'{2 ** suma}'

  if suma != limite:
    resultado += ' '

  suma += 1

print(resultado)
