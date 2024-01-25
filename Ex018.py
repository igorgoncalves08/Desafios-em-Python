import math
ang = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Seno do angulo {} é {:.2f}'.format(ang, seno))
print('Cosseno do angulo {} é {:.2f}'.format(ang, cos))
print('A tangente do angulo {} é {:.2f}'.format(ang, tang))
