angle = float(input('Ingrese un ángulo: '))

if angle == 0:
  print(f'El ángulo de {angle}º ({angle} grados), es nulo')

if angle == 180:
  print(f'El ángulo de {angle}º ({angle} grados), es llano')

if angle == 90:
  print(f'El ángulo de {angle}º ({angle} grados), es recto')

if angle > 0 and angle < 90:
  print(f'El ángulo de {angle}º ({angle} grados), es agudo')

if angle > 90 and angle < 180:
  print(f'El ángulo de {angle}º ({angle} grados), es obtuso')

if angle > 180:
  print('Ángulo no válido')
