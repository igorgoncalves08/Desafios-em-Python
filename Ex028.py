from random import randint
escolhido = randint(0, 5)
print('Vou pensar em um numero de 0 a 5 e quero que você descubra qual e o numero')
numero = int(input('Digite o numero que você acha que é: '))
if numero == escolhido:
    print('Parabens você ACERTOU !!!')
else:
    print('Você ERROU !!!')