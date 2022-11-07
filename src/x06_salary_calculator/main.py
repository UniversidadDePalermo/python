def main():
  '''
  Ingrese el valor de una hora de trabajo: 150.00
  Ingrese la cantidad de horas trabajadas al mes: 120
  El sueldo por 120 al mes es de 18000.0 AR$
  '''
  valor_hora = input('Ingrese el valor de una hora de trabajo: ')
  cantidad_horas = input('Ingrese la cantidad de horas trabajadas al mes: ')
  sueldo = float(valor_hora) * int(cantidad_horas)

  print(f'El sueldo por {cantidad_horas} al mes es de {sueldo} AR$')
