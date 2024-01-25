dia = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foi rodado com o carro? '))
valor = dia * 60 + km * 0.15
print('O total a pagar é: R$ {}'.format(valor))
