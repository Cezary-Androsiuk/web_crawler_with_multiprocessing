from imports import *

def single_process(pages):
    print('\trunning singleprocess crawler')
    book_title = []
    star_rating = []
    product_price = []

    sleep_time_sum = 0

    for page in pages:
        sleep_time = random.randint(2,6) # prevent IP ban
        print('\tpage:', page, 'sleep:', sleep_time)
        time.sleep(sleep_time)
        sleep_time_sum += sleep_time
        
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        results = requests.get(url)
        soup = BeautifulSoup(results.text, 'html.parser')

        book_div = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

        for container in book_div:
            title = container.article.h3.a['title']
            book_title.append(title)

            rating = container.article.p['class'][-1]
            star_rating.append(rating)

            price = container.article.find('div', class_='product_price').p.text[2:]

            product_price.append(price)
        
        # pages separator
        book_title.append(' '); star_rating.append(' '); product_price.append(' ')
    return (book_title, star_rating, product_price, sleep_time_sum)