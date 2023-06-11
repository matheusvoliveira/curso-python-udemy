import requests
import bs4
# import scrapy
#
# class Olx():
#     name = 'olx'
#     start_url = ['https://www.olx.com.br/estado-mg?q=xbox%20one']
#
#     def parse():
#         for i in response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/div/div/div/ul'):
#             info = i.xpath('/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/div/div/div/ul').getall()
#
#         print(info)
#
# olx = Olx
# olx.parse()

def authors():
    print(8*'-')
    print('\nauthors\n'.upper())
    print(8 * '-')
    pages = 1
    url = 'https://www.olx.com.br/videogames?q=xbox%20one&op=2&opst=2'
    response_authors = requests.get(url)
    soup_authors = bs4.BeautifulSoup(response_authors.text, 'lxml')
    print(response_authors)
    authors = soup_authors.select('.sc-1fcmfeb-2.dvcyfD')
    print(authors)

authors()