from math import sqrt

n=16
b=9.75
suma = 0
for j in range(9):
    i = int(input('i: '))
    hi = int(input('hi: '))
    suma = suma + hi*(i-b)**2

contraste = sqrt(suma/n)
print(contraste)
