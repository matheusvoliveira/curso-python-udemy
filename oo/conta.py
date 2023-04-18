# Em Python, "self" é uma convenção usada para se referir ao
# objeto atual de uma classe. Em outras palavras, é uma referência ao próprio objeto.
# uma classe abriga varios objetos

class Conta:
#__init__ é uma função construtora que aloca todos os atributos
    def __init__(self, numero, titular, saldo, limite): # atributos
        print('esta é a conta {} '.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.method_count = 0

    def extrato(self): #metodos todos que tem def
        print(f'saldo {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor
        self.method_count += 1

    def __pode_sacar(self, valor):
         if (valor - self.__saldo) <= 0:
             return (valor - self.__saldo) <= 0
    def saca(self,valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            self.method_count += 1
        else:
            print(f'O valor R${valor} deixa o saldo da sua conta negativo!')


    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    # não inclui o method_count porque ele já é chamado no saca() então ele iria ser chamado duas vezes


    def inadimplencia(self):
        if self.__saldo <= 100:
            print(f'{self.__titular } é inadimplente!')
        else:
            print(f'{self.__titular} não é inadimplente!')
        return self.__saldo <= 100

    def cartao_credito(self):
        if self.method_count >= 2 and not self.inadimplencia():
            print('Você esta elegivel para o cartão!')
        else:
            print('Movimente mais a sua conta e tente de novo!')

    def get_saldo(self):
        return self.__saldo # get são metodos que recolhem um dado e o retornam como esse que retorna o saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    # def set_limite(self, novo_limite): #set são todos os metodos que mudam os dados, nesse caso ele redefine o limite
    #     self.__limite = novo_limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
        return self.__limite


    @staticmethod    #methodo da classe Conta não do objeto conta
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

# conta = Conta(123, 'Matheus', 1000, 2000)
# conta2 = Conta(786, 'Rodrigo', 500, 5000)
# conta2.inadimplencia()
# conta2.cartao_credito()
# print(conta2.method_count)
# conta2.saca(10)
# print(conta2.method_count)
# conta2.cartao_credito()
