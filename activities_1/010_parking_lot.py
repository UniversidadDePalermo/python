# Valor de una hora de estacionamiento
VALOR_HORA = 45

minutos = int(input('Ingrese minutos de uso: '))
horas = minutos / 60
exceso = horas - int(horas)
minutos_extra = exceso * 60

# Se calculan las horas diviendo el numero de minutos entre 60.
# Si la division es exacta, no hay minutos extra que considerar
# Si la division no es exacta, se deben tomar los minutos multiplicando
# la parte decimal por 60
if minutos_extra >= 15:
  total_a_pagar = (horas * VALOR_HORA) + VALOR_HORA
  print(f'El total a pagar por {int(horas)} horas y {int(minutos_extra)} minutos es de {total_a_pagar} AR$')
else:
  total_a_pagar = horas * VALOR_HORA
  print(f'El total a pagar por {int(horas)} horas y {int(minutos_extra)} minutos es de {total_a_pagar} AR$')
