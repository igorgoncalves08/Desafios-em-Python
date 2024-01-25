salario = float(input('Informe o sálario do funcionario: '))
if salario <= 1250:
    calculo = salario * 1.15
    print('Este funcionario terá um aumento de 15% e seu novo salario sera de {:.2f} R$'.format(calculo))
else:
    conta = salario * 1.10
    print('Este funcionario terá um aumento de 10% e seu novo salario será de {:.2f} R$'.format(conta))

