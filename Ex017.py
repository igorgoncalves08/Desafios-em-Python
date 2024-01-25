import math
c1 = float(input('Digite o valor do Cateto Oposto: '))
c2 = float(input('Digite o valor do Cateto Adjacente: '))
h = math.hypot(c1, c2)
print('O comprimento da Hipotenusa é: {:.2f}'.format(h))

