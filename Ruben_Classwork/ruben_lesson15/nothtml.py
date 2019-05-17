from bs4 import BeautifulSoup
from urllib import request
import csv
import re


url = 'https://list.am'

data = request.urlopen(url).read()
bs = BeautifulSoup(data, 'lxml')

div_c = bs.find_all('div', class_=re.compile('c c[1|2|3]'))


csv_file = open('db.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

for idx, item in enumerate(div_c):
    product = item.find('div')
    hot = item.find('span')

    link = item.find('a').get('href')

    item_data = request.urlopen("{}{}".format(url, link)).read()
    item_bs = BeautifulSoup(item_data, 'lxml')

    author = item_bs.find('a', class_='l').text

    phone_button = item_bs.find('div', class_='phone')
    phone_url = phone_button.find('a').get('onclick').split(',')[1].strip('\'')

    phone_data = request.urlopen("{}{}".format(url, phone_url)).read()
    phone_bs = BeautifulSoup(phone_data, 'lxml')

    phone_links = phone_bs.find('div', class_='phones').find_all('a')

    numbers = []
    for phone_link in phone_links:
        numbers.append(phone_link.text)

    csv_writer.writerow((product.text, author, numbers, bool(hot)))

    print('Processed {} products'.format(idx))
