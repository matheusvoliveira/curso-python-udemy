class Programa:
#uma classe mãe que deixa alguns atributos pre atribuidos para nao ser nescessario atribuir em todas class - Herança
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self.__likes = 0
    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        #super() chama o init da classe mãe com os atributos nome e ano eles não precisam ser declarados de novo.
        self.duracao = duracao



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')