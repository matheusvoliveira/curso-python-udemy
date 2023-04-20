class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0
    def dar_like(self):
        self.likes += 1


class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.likes = 0

    def dar_like(self):
        self.likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print('Nome:  {}  - Ano:  {}  - Duração: {}  Likes:  {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao,
                                                             vingadores.likes))

atlanta = Serie('Atlanta', 2017, 4)
atlanta.dar_like()
atlanta.dar_like()
print('Nome:  {}  - Ano:  {}  - Temporadas:  {}  Likes:  {}'.format(atlanta.nome, atlanta.ano, atlanta.temporada,
                                                                    atlanta.likes))