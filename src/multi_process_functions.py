from imports import *

def generate_urls(pages):
    url_list = []
    for page in pages:
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        url_list.append(url)
    return url_list

def scrape_url(url):
    book_title = []
    star_rating = []
    product_price = []
    
    # trim url to print only page number
    page = url
    patterns_to_remove = ['http://books.toscrape.com/catalogue/page-', '.html']
    for pattern in patterns_to_remove:
        page = page.replace(pattern, '')
    

    sleep_time = random.randint(2,6)
    print('\tpage:', page, 'sleep:', sleep_time)
    time.sleep(sleep_time)

    results = requests.get(url)
    
    soup = BeautifulSoup(results.text, 'html.parser')

    book_div = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for container in book_div:
        title = container.article.h3.a['title'] # take 'title' parameter
        book_title.append(title)
        
        rating = container.article.p['class'][-1] # take 'class' parameter and from class parameter take last value
        star_rating.append(rating)
        
        price = container.article.find('div', class_='product_price').p.text[2:] # take 'X' from <p>X</p> and then trim first two signs 'Â£'
        product_price.append(price)

    book_title.append(' '); star_rating.append(' '); product_price.append(' ')
    return (book_title, star_rating, product_price, sleep_time)
