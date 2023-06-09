# calcular o valor do aluguel de um carro sendo que o dia custa R$60 e cada km rodado R$0,15
def aluguel(km, dias):
    valor_dia = dias * 60
    valor_km = km * 0.15
    return valor_dia + valor_km
