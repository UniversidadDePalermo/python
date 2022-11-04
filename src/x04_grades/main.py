def main():
  '''
  Leer 3 notas,
    - Sí el promedio es mayor a 9, Abanderado
    - Sí el promedio da: 7 o más, Aprobado
    - Sí el promedio es aplazo (<4), Marzo
    - Sí la tercer nota es menor a 7, Diciembre
  '''

  nota_1 = int(input('Ingrese la primer nota: '))
  nota_2 = int(input('Ingrese la segunda nota: '))
  nota_3 = int(input('Ingrese la tercer nota: '))

  if (nota_1 > 10 or nota_1 < 0) or (nota_2 > 10 or nota_2 < 0) or (nota_3 > 10 or nota_3 < 0):
    print('Valores invalidos')
  else:
    promedio = (nota_1 + nota_2 + nota_3) / 3

    if promedio > 8:
      print('Abanderado')
    elif promedio >= 7:
      print('Aprobado')
    elif promedio > 5 and nota_3 < 7:
      print('Diciembre')
    else:
      print('Marzo')
