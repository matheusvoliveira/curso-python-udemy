import scrapy

class Olx():
    name = 'olx'
    start_url = ['https://www.olx.com.br/estado-mg?q=xbox%20one']

    def parse():
        for i in response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/div/div/div/ul'):
            info = i.xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/div/div/div/ul').getall()

        print(info)

olx = Olx
olx.parse()