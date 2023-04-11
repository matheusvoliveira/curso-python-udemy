# # Em Python, "self" é uma convenção usada para se referir ao
# # objeto atual de uma classe. Em outras palavras, é uma referência ao próprio objeto.
# # uma classe abriga varios objetos
# class Conta:
#     def __init__(self, numero, titular, saldo, limite = 1000.0):  #atributos
#         print('contruindo objeto...{} '.format(self))
#         self.numero = numero
#         self.titular = titular  #__init__ é uma função construtora que aloca todos os atributos
#         self.limite = limite
#         self.saldo = saldo
#
#
# conta = Conta(123, "Matheus", 100.0)
# conta2 = Conta(321, "Maricos", 800.0, 2000.0)
# print(conta.saldo)
# print(conta2.numero, conta.titular)
#

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('esta é a conta {} '.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


conta = Conta(123, 'Matheus', 1000, 2000)
print(conta.limite)