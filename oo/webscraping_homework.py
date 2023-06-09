import requests
import bs4
import pdb


def authors():
    print(8*'-')
    print('\nauthors\n'.upper())
    print(8 * '-')
    pages = 1
    url = f'https://quotes.toscrape.com/page/{pages}/'
    response_authors = requests.get(url)
    soup_authors = bs4.BeautifulSoup(response_authors.text, 'lxml')
    authors = soup_authors.select('.author')


    for author in authors:
        print(author.contents[0])


def tags():
    print(8*'-')
    print('\ntags\n'.upper())
    print(8 * '-')
    response_tag = requests.get('http://quotes.toscrape.com/')
    soup_authors = bs4.BeautifulSoup(response_tag.text, 'lxml')
    tags = soup_authors.select('.tag')

    for tag in tags[:9]:
        print(tag.contents[0])

def quotes():
    print(8 * '-')
    print('\nquotes\n'.upper())
    print(8 * '-')
    response_quotes = requests.get('http://quotes.toscrape.com/')
    soup_quotes = bs4.BeautifulSoup(response_quotes.text,'lxml')
    quotes = soup_quotes.select('.text')

    for quote in quotes:
        print(quote.contents[0])


authors()
quotes()
tags()