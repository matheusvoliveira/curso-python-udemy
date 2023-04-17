
class Clientes:
    def __init__(self, nome):
        self.nome = nome

    # porque usar o @property ao invez de um atributo
    # porque com a propriedade voce pode aplicar logica costumizada
    @property
    def nome(self):
        print('chamando @property nome')
        if len(self.name) >= 2:
            return self.nome.title()
        else:
            print('Nome invalido')
    @nome.setter
    def nome(self,nome):
        print('chamando setter nome()')
        self.nome = nome

