import requests


currency = int(input('Escolha a moeda que quer a cotação(ex: USD, GBP, EUR): '.upper().strip()))
value = float(input('Escolha o valor a ser cotado: '))
api_key = '153b123b4ebae7568cba4da4'
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}'
# {currency} na url mostra qual moeda ele vai pegar a cotação
response = requests.get(url)
data = response.json()
#reponse.json() mostra todos os atributos de uma biblioteca
cotation = data['conversion_rates']['BRL']

if cotation > value:
    print(cotation / value)
