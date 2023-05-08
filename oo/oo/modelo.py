class Programa:
#uma classe mãe que deixa alguns atributos pre atribuidos para nao ser nescessario atribuir em todas class - Herança
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self.__likes = 0

    # def imprime(self):
    #     print(f'Nome: {self.nome} Likes: {self.likes}')

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome
    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        #super() chama o init da classe mãe com os atributos nome e ano eles não precisam ser declarados de novo.
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao}min - Likes: {self.likes}'

    # def imprime(self):
    #     print(f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}')

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas


    @property
    def tamanho(self):
        return len(self.programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 3)
# print(vingadores.nome)
vingadores.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
filmes_e_series = [vingadores, atlanta, tmep, demolidor]


findis = Playlist('Findis', filmes_e_series)
for programa in findis.listagem:
    print(programa)

print(f'Tamanho: {len(findis.listagem)}')