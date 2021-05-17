valor1, valor2, valor3 = input().split()

A = int(valor1)
B = int(valor2)
C = int(valor3)

maiorAB = (A + B + abs(A - B)) / 2

if maiorAB > C:
    print('{:.0f}'.format(maiorAB), "eh o maior")
else:
    print(C, "eh o maior")