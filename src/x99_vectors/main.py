def main():
  '''
  Se ingresan números hasta que se llene 1 vector de 10 elementos
  de números pares mayores e iguales a 12 y menores a 60 (VECTOR A)

  a) Se genera otro vector con los valores que son superiores al promedio (VECTOR B)
  b) Se genera otro vector con las posiciones que son inferiores a la posición del máximo (VECTOR C)
  c) En el vector B insertar después de cada elemento mayor a 20 el numero 999
  d) En el vector C insertar antes de cada elemento múltiplo de 7 en subíndice impar, el numero 222
  e) Eliminar del vector C los números que no sean 222
  f) Ordenar de menor a mayor de forma programática los números del vector A

  - Cada ítem solicitado se pide una vez realizado mostrarlo mediante función
    programática.

  ```
  Lote de prueba

  A = [12, 40, 14, 28, 50, 56, 58, 16, 20, 36]
  promedio = 33

  B = [40, 50, 56, 58, 36]
  pos_max = 6

  C = [12, 40, 14, 28, 50, 56]

  # punto c
  B = [40, 999, 50, 999, 56, 999, 36, 999]

  # punto d
  C = [12, 40, 14, 222, 28, 50, 56]

  # punto e
  C = [222]

  # punto f
  A = [12, 14, 16, 20, 28, 36, 40, 50, 56, 58]
  ```
  '''
  vector_a = make_vector_a()
  debug_vec(vector_a)
  vector_b = make_vector_b(vector_a)
  debug_vec(vector_b)
  vector_c = make_vector_c(vector_a)
  debug_vec(vector_c)
  vector_b = add_nine_hundred_ninety_nine(vector_b)
  debug_vec(vector_b)
  vector_c = add_two_hundred_twenty_two(vector_c)
  debug_vec(vector_c)
  vector_c = remove_not_two_hundred_twenty_two(vector_c)
  debug_vec(vector_c)
  vector_a.sort()
  debug_vec(vector_a)

def make_vector_a():
  '''
  Crea el vector A.
  Este vector solo admite numeros mayores o iguales a 12 y menores a 60
  '''
  vector = []

  while len(vector) < 10:
    value = int(input('Ingrese un número: '))
  
    if value >= 12 and value < 60:
      vector.append(value)
    else:
      print(f'El valor "{value}", no es válido. Debes ingresar un valor mayor o igual a 12 y menor a 60.')

  return vector

def promedio(vec):
  '''
  Se calcula agregando un grupo de números y dividiendo por el recuento de estos
  números.

  Por ejemplo:

  - Teniendo: 2, 3, 3, 5, 7, 10
  - Recuento: 6
  - Agregado: 30
  - Promedio: 5
  '''
  sum = 0

  for el in vec:
    sum += el
  
  return sum / len(vec)

def make_vector_b(vec):
  '''
  Crea el vector B.
  Este vector contiene solo los valores que son mayores al promedio del vector
  dado
  '''
  prom = promedio(vec)
  vec_b = []

  for el in vec:
    if el > prom:
      vec_b.append(el)

  return vec_b

def get_max_value_pos(vec):
  '''
  Obtiene el índice del elemento de mayor valor en el vector
  '''
  max = vec[0]
  max_pos = 0

  for idx in range(len(vec)):
    if vec[idx] > max:
      max = vec[idx]
      max_pos = idx

  return max_pos

def make_vector_c(vec):
  '''
  Crea el vector C.

  El vector C solo contiene elementos del vector dado, cuyo valor es menor
  al elemento de mayor valor en el vector dado.

  Nota: Solo se toman los valores hasta el índice del valor mayor, dado que en
  el enunciado se muestra: `[12, 40, 14, 28, 50, 56]` que no contiene los
  valores: `[12, 40, 14, 28, 50, 56, 16, 20, 36]`
  '''
  vec_c = []
  max_value_pos = get_max_value_pos(vec)
  max_val = vec[max_value_pos]

  for idx in range(len(vec)):
    if vec[idx] < max_val and idx <= max_value_pos:
      vec_c.append(vec[idx])

  return vec_c

def add_nine_hundred_ninety_nine(vec):
  '''
  Crea un vector donde el numero "999" es insertado después de cada elemento
  cuyo valor es mayor a 20
  '''
  vec_b = []

  for el in vec:
    vec_b.append(el)

    if el > 20:
      vec_b.append(999)

  return vec_b

def add_two_hundred_twenty_two(vec):
  '''
  Crea un vector donde se agrega el numero "222" antes de cada elemento cuyo
  valor sea un multiplo de 7 y a la vez sea de subindice impar.
  '''
  vec_b = []

  for idx in range(len(vec)):
    if idx % 2 != 0 and vec[idx] % 7 == 0:
      vec_b.append(222)
      vec_b.append(vec[idx])
    else:
      vec_b.append(vec[idx])

  return vec_b

def remove_not_two_hundred_twenty_two(vec):
  '''
  Crea un vector con solo los elementos cuyo valor sea "222"
  '''
  vec_b = []

  for el in vec:
    if el == 222:
      vec_b.append(el)

  return vec_b

def debug_vec(vec):
  '''
  Muestra el array con su índice
  '''
  out = ''

  for idx in range(len(vec)):
    out += f'{idx}: {vec[idx]}\t'

  print(out)
