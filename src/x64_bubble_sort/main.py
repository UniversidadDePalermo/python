# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped := false
#         for i := 1 to n-1 inclusive do
#             /* if this pair is out of order */
#             if A[i-1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap(A[i-1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure
def bubble_sort(vec):
  '''
  Organiza numeros en un vector usando el algoritmo "Bubble Sort"

  Referencia: https://en.wikipedia.org/wiki/Bubble_sort
  '''
  clone = vec

  for idx in range(0, len(vec) - 1):
    for sub_idx in range(idx + 1, len(vec)):
      if vec[idx] > vec[sub_idx]:
        swap(clone, idx, sub_idx)

  return clone

def swap(vec, x, y):
  '''
  Intercambia los elementos en los índices entregados
  '''
  temp = vec[x]
  vec[x] = vec[y]
  vec[y] = temp
