from math import sqrt

cateto_opuesto = input('Ingrese el valor del cateto opuesto: ')
cateto_adyacente = input('Ingrese el valo del cateto adyacente: ')

cateto_opuesto = float(cateto_opuesto)
cateto_adyacente = float(cateto_adyacente)

hypotenusa = cateto_opuesto ** 2 + cateto_adyacente ** 2
hypotenusa = sqrt(hypotenusa)

print(f'La hypotenusa de un triangulo rectángulo con catetos: ')
print(f'Cateto Opuesto: {cateto_opuesto}')
print(f'Cateto Adyacente: {cateto_adyacente}')
print(f'Es: {hypotenusa}')
