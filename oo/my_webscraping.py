import requests
import bs4
import pdb


result = requests.get('http://www.example.com')
type(result)
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

title = soup.select('title')
paragraphs = soup.select('p')

pdb.set_trace()

res = requests.get('https://pt.wikipedia.org/wiki/Odd_Taxi')
soup = bs4.BeautifulSoup(res.text, 'lxml')
toc = soup.select('toctext')
