n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas é: ', n.upper())
print('Seu nome com todas as letras minúsculas é: ', n.lower())
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))






