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

    def extrato(self): #metodo 
        print(f'saldo {self.saldo} do titular {self.titular}')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor


conta = Conta(123, 'Matheus', 1000, 2000)
conta2 = Conta(786, 'Rodrigo', 500, 5000)

conta.deposita(500)
print(conta2.extrato())
print(conta.extrato())
conta.saca(100)
print(conta.extrato())