import requests
from bs4 import BeautifulSoup
import json

URL = 'https://bookwyrm.social/user/rmcminds/books/read?sort=-finish_date'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

books = soup.find_all('tr', class_='book-preview')

data = []
for book in books[:5]:  # only take the first 5 books
    title_link = book.find('td', {'data-title': 'Title'}).find('a')
    title = title_link.text
    link = "https://bookwyrm.social" + title_link['href']
    author_link = book.find('td', {'data-title': 'Author'}).find('a')
    author = author_link.text
    img_url = book.find('img', class_='book-cover')['src']
    data.append({'title': title, 'link': link, 'img_url': img_url, 'author': author})

with open('assets/read.json', 'w') as f:
    json.dump(data, f)


URL = 'https://bookwyrm.social/user/rmcminds/books/reading?sort=-start_date'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

books = soup.find_all('tr', class_='book-preview')

data = []
for book in books:
    title_link = book.find('td', {'data-title': 'Title'}).find('a')
    title = title_link.text
    link = "https://bookwyrm.social" + title_link['href']
    author_link = book.find('td', {'data-title': 'Author'}).find('a')
    author = author_link.text
    img_url = book.find('img', class_='book-cover')['src']
    data.append({'title': title, 'link': link, 'img_url': img_url, 'author': author})

with open('assets/reading.json', 'w') as f:
    json.dump(data, f)
