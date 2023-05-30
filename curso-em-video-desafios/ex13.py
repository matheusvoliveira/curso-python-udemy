salario = float(input('Insira o salario do funcionario: '))
aumento = int(input('Insira a % de aumento: '))
porcentagem_aumento = (1.0 + (aumento/100)) * salario
print('O salario com aumento de {}% fica R${:.2f}'.format(aumento, porcentagem_aumento))