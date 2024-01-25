distancia = int(input('Qual a distância da viagem em Km ?'))
if distancia <= 200:
    preco = distancia * 0.50
    print('O valor da passagem será {} R$'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem será {} R$'.format(preco))
    