import requests
import bs4
import pdb


url = 'https://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(len(soup.select('.product_pod')))

products = soup.select(('.product_pod'))
example = products[0]
example.select('.star-rating.Three')



two_star_titles = []

for n in range(1,10):
    scrape_url = url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
pdb.set_trace()

