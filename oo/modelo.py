class Programa:
#uma classe mãe que deixa alguns atributos pre atribuidos para nao ser nescessario atribuir em todas class - Herança
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def imprime(self):
        print(f'Nome: {self.nome} Likes: {self.likes}')

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

    def imprime(self):
        print(f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}')

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
# print(vingadores.nome)
vingadores.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()