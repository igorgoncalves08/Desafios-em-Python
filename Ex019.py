import random
n1 = input('Digite o nome do primeiro aluno(a): ')
n2 = input('Digite o nome do segundo aluno(a): ')
n3 = input('Digite o nome do terceiro aluno(a): ')
n4 = input('Digite o nome do quarto aluno(a): ')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print('O aluno(a) sorteado foi {}'.format(sorteio))
