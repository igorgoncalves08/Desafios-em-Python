velocidade = int(input('Digite a velocidade que o carro ultrapassou: '))
if velocidade > 80:
    print('Você foi multado!!!')
    multa = (velocidade - 80) * 7
    print('Você terá que pagar {} R$ de multa.'.format(multa))
else:
    print('Você não foi multado!!!')

