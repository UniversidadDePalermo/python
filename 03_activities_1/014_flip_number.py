numero = int(input('Ingresar numero de 2 cifras: '))

if numero > 100:
  print(f'El número "{numero}", tiene más de 2 cifras')
else:
  primer_digito = int((numero / 10) % 10)
  segundo_digito = numero % 10

  if numero > 50:
    print(f'{segundo_digito}{primer_digito}')
  else:
    print(f'{primer_digito}; {segundo_digito}')
