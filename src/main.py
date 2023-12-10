# python -m venv env
# env\Scripts\activate
# pip install -r requirements.txt
# python src\main.py
# deactivate

from imports import *
from single_process import single_process
from multi_process import multi_process
    


def printResult(start, end, books, out_file):
    print('\tIt took', (end-start), 'seconds, but sleep time took', (books[3]), 'seconds\n')

    
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as fp:
        for (item1, item2, item3) in zip(books[0], books[1], books[2]):
            fp.write("%s  " % item1)
            fp.write("%s  " % item2)
            fp.write("%s\n" % item3)


if __name__ == '__main__':
    single_process_exec_times = []
    single_process_sleep_times = []
    multi_process_exec_times = []
    multi_process_sleep_times = []
    pages_counts = []

    for i in range(2, 12, 1):
        # pages = np.arange(1,51,1)
        pages = np.arange(1,i,1)
        print('pages to crawl', pages[-1], end='\n\n')
        pages_counts.append(i)
        
        start = time.time()
        books = single_process(pages)
        end = time.time()
        printResult(start, end, books, 'output/single_process_out.txt')
        single_process_exec_times.append(end-start)
        single_process_sleep_times.append(books[3])
                
        start = time.time()
        books = multi_process(pages)
        end = time.time()
        printResult(start, end, books, 'output/multi_process_out.txt')
        multi_process_exec_times.append(end-start)
        multi_process_sleep_times.append(books[3])

    import matplotlib.pyplot as plt
    plt.plot(pages_counts, single_process_exec_times, label='single_process', marker='o')
    plt.plot(pages_counts, multi_process_exec_times, label='multi_process', marker='x')

    # Dodaj etykiety osi, tytuł wykresu i legendę
    plt.xlabel('Ilość stron do odczytania')
    plt.ylabel('czas (s)')
    plt.title('Wykres wykres czasu do ilości stron www')
    plt.legend()

    # Wyświetl wykres
    plt.show()