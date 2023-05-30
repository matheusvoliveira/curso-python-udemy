numero = int(input('Digite o numero que quer saber a tabuada: '))
for x in range(1, 11):
    print('{} x {} = {}'.format(numero, x, numero * x))