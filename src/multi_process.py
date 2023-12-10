from imports import *

from multi_process_functions import (
    generate_urls,
    scrape_url
)

def multi_process(pages):
    freeze_support() # help by waiting for a process if is not main process
    url_list = generate_urls(pages)

    cores = cpu_count()
    # limit cores 
    if(cores > len(url_list)):
        cores = len(url_list)
    print('\trunning multiprocess crawler with', cores, 'cores from', cpu_count(), 'available cores')


    p = Pool(cores)
    book_list = p.map(scrape_url, url_list)
    p.terminate() # mark all processes as ended to join them
    p.join()

    book_title = []
    star_rating = []
    product_price = []
    sleep_time_sum = 0

    for book in book_list:
        for bt in book[0]:
            book_title.append(bt)
        # print(book[0], end="\n\n")
        for sr in book[1]:
            star_rating.append(sr)
        # print(book[1], end="\n\n")
        for pr in book[2]:
            product_price.append(pr)
        # print(book[2], end="\n\n")
        sleep_time_sum += book[3]
        # print(book[3], end="\n\n")

    return (book_title, star_rating, product_price, sleep_time_sum)