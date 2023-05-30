salario = float(input('Insira o preço do seu salario: '))
aumento = int(input('Insira a % de aumento: '))
porcentagem_aumento = (1.0 - (aumento/100)) * salario
print('O salario com aumento de {}% custa R${:.2f}'.format(aumento, porcentagem_aumento))