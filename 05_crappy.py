#5# Solucion mas chota imposible

F = [1, 2, 3, 1, 4, 1, 4]
valor_min = None
for num in F:
    if valor_min == None or num < valor_min:
        valor_min = num
i = 0
for num in F:
    if valor_min == num:
        print(f"El valor que ocupa el minimo es: [{i}]")
    i +=1
