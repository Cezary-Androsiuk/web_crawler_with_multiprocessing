# python -m venv env
# env\Scripts\activate
# pip install -r requirements.txt
# deactivate

import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import time
import random

pages = np.arange(1,51,1)

book_title = []
star_rating = []
product_price = []

start = time.time()
for page in pages:
    time.sleep(random.randint(1,10))
    
    url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')

    book_div = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for container in book_div:
        title = container.article.h3.a['title']
        book_title.append(title)

        price = container.article.find('div', class_='product_price').p.text
        product_price.append(price)

        rating = container.article.p['class'][-1]
        star_rating.append(rating)

end = time.time()
print('It took', (end-start), 'seconds')