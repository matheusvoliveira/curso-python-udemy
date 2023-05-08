class Data:
    def __init__(self, dia, mes, ano,):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')

d = Data(27,11, 2007)
d.formata()