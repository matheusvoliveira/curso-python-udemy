import requests
import bs4
import pdb


result = requests.get('http://www.example.com')
type(result)
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

title = soup.select('title')
paragraphs = soup.select('p')


res = requests.get('https://pt.wikipedia.org/wiki/Odd_Taxi')
soup = bs4.BeautifulSoup(res.text, 'lxml')
toc = soup.select('toctext')

res = requests.get('https://pt.wikipedia.org/wiki/Edgars_Rink%C4%93vi%C4%8Ds')

soup = bs4.BeautifulSoup(res.text,'lxml')
img = soup.select('.floatnone')

president = soup.select('.floatnone')[0]



pdb.set_trace()