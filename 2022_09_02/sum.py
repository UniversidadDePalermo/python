numero_1 = int(input('Ingrese un numero: '))
numero_2 = int(input('Ingrese un segundo numero: '))

contador = numero_1 + 1
acc = 0

while contador < numero_2:
  acc = acc + contador
  contador = contador + 1

print(f'La suma es: {acc}')
