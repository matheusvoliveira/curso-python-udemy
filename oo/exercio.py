class Biblioteca:
    def __init__(self, pessoa, acervo=None):
        self.pessoa = pessoa
        self.acervo = [] if acervo is None else [acervo]

    def pegar_emprestado(self, emprestado):
        self.acervo.append(emprestado)

    def mostrar(self):
        print(self.pessoa, self.acervo)

clara = Biblioteca('Clara')
clara.pegar_emprestado('Percy Jackson')
clara.mostrar()
clara.pegar_emprestado('Capitães de areia')
clara.mostrar()

