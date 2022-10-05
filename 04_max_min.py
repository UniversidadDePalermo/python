#4#
F = [4, 5, 1, 2, 3]

maximo = None
for i in F:
    if maximo == None or i > maximo:
        maximo = i
print(maximo)

minimo = None
for i in F:
    if minimo == None or i < minimo:
        minimo = i
print(minimo)

#4# OTRA FORMA

F = [1, 2, 3]
maximo = max(F)
minimo = min(F)
print(f"El valor maximo es: {maximo}")
print(f"El valor minimo es: {minimo}")
