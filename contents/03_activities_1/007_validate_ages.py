persona_1 = input('Ingrese la edad de la primera persona: ')
persona_2 = input('Ingrese la edad de la segunda persona: ')

persona_1 = int(persona_1)
persona_2 = int(persona_2)

if (persona_1 >= 18 and persona_2 < 18) or (persona_1 < 18 and persona_2 >= 18):
  # calcular promedio
  promedio = (persona_1 + persona_2) / 2
  print(f'El promedio de la edad de las 2 personas es: {promedio}')
else:
  print(f'La primera persona tiene {persona_1} años')
  print(f'La segunda persona tiene {persona_2} años')
