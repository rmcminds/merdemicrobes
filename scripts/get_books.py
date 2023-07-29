import sys
import requests
from bs4 import BeautifulSoup
import json

read_url = 'https://bookwyrm.social/user/rmcminds/books/read?sort=-finish_date'
reading_url = 'https://bookwyrm.social/user/rmcminds/books/reading?sort=-start_date'

payload = {
    'localname': sys.argv[1],
    'password': sys.argv[2]
}

# log in and retrieve html from both read and reading pages
with requests.Session() as s:
    payload['csrfmiddlewaretoken'] = s.get('https://bookwyrm.social/').cookies['csrftoken']
    p = s.post('https://bookwyrm.social/login?next=/', data=payload)
    read_books_page = s.get(read_url)
    reading_books_page = s.get(reading_url)

# parse read books html
read_books = BeautifulSoup(read_books_page.content, 'html.parser').find_all('tr', class_='book-preview')
data = []
for book in read_books:
    title_link = book.find('td', {'data-title': 'Title'}).find('a')
    title = title_link.text
    link = "https://bookwyrm.social" + title_link['href']
    author = book.find('td', {'data-title': 'Author'}).find('a').text
    date_finished = book.find('td', {'data-title': 'Started'}).nextSibling.text.strip('\n ')
    rating = book.find('td', {'data-title': 'Rating'}).text.strip('\n ')
    img_url = book.find('img', class_='book-cover')['src']
    data.append({
      'title': title,
      'link': link,
      'img_url': img_url,
      'author': author,
      'date_finished': date_finished,
      'rating': rating,
    })

with open('_data/read.json', 'w') as f:
    json.dump(data, f)

# parse reading books html
reading_books = BeautifulSoup(reading_books_page.content, 'html.parser').find_all('tr', class_='book-preview')
data = []
for book in reading_books:
    title_link = book.find('td', {'data-title': 'Title'}).find('a')
    title = title_link.text
    link = "https://bookwyrm.social" + title_link['href']
    author = book.find('td', {'data-title': 'Author'}).find('a').text
    date_started = book.find('td', {'data-title': 'Started'}).text.strip('\n ')
    img_url = book.find('img', class_='book-cover')['src']
    data.append({
      'title': title,
      'link': link,
      'img_url': img_url,
      'author': author,
      'date_started': date_started,
    })

with open('_data/reading.json', 'w') as f:
    json.dump(data, f)
