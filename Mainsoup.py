import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    session = requests.session()
    session.headers = {
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    r = session.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def write_csv(data):
    with open('realtytrac.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow((data['adress'],
                         data['url'],
                         data['price'],
                         data['date']))


def fix_price(text):
    price = text.split('$')
    price = price[1].replace(',', '')
    return price


def fix_date(text):
    date = text.split(' ')
    date = date[3]
    return date


def get_page_data(html, url):
    soup = BS(html, 'lxml')

    try:
        adress = soup.find('section', class_='summary-block').find('h1')
        adresses = adress.find_all('span')
        adress = adresses[0].text + ' ' + adresses[1].text + ' ' + adresses[2].text + ' ' + adresses[3].text
    except:
        adress = ''

    try:
        prices = soup.find('div', class_='price').find('strong').text
        price = fix_price(prices)
    except:
        price = ''

    try:
        dates = soup.find('div', class_='col-3').find('a').text.strip()
        date = fix_date(dates)
    except:
        date = ''

    data = {'adress': adress,
            'url': url,
            'price': price,
            'date': date}

    write_csv(data)


def main():
    #   url = 'https://www.realtytrac.com/propertydetails/pa/tarentum/15084/johnson-ave/109435477/'
    url = input('Введите ссылку: ')
    get_page_data(get_html(url), url)


if __name__ == '__main__':
    main()
