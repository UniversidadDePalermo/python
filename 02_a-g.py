#2#

arreglo = [1,2,3,4,5,6,7,8,9,0]
#a#
print(arreglo[3])
#b#
arreglo.reverse()
print(arreglo)
#c#
print(arreglo[0]*arreglo[-1])
#d#
for i in arreglo:
    if i%2 == 1:
        print(i, end=" ")
#e#
o_suma = 0
for o in arreglo:
    if o%2 == 0:
        o_suma += o
print("\n",o_suma)
#f#
i_multiply = 1
for i in arreglo:
    if i%2 == 1:
        i_multiply *= i
print(i_multiply)
#g#
arreglo[0], arreglo[-1] = arreglo[-1], arreglo[0]
print(arreglo)
