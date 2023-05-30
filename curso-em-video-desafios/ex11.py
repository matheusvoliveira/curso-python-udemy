class Parede:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.area = self.largura * self.altura


    def get_area(self):
        print('Sua parede tem a dimensão de {} x {} e sua áreaé de de {:.2f}m²'.format(self.largura, self.altura,
                                                                                       self.area))
    def quantidade_tinta(self):
        litros = self.area / 2
        print(f'Para pintar a parede você precisará de {litros :.2f}l de tinta')

parede = Parede(1.67, 5.78)
parede.get_area()
parede.quantidade_tinta()
