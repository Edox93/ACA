from bs4 import BeautifulSoup
from urllib import request
# import csv
import sqlite3
import re


conn = sqlite3.connect('listam.db')
cur = conn.cursor()

url = 'https://list.am'

data = request.urlopen(url).read()
bs = BeautifulSoup(data, 'lxml')

div_c = bs.find_all('div', class_=re.compile('c c[1|2|3]'))


# csv_file = open('db.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)

for idx, item in enumerate(div_c):
    product = item.find('div')
    hot = item.find('span')

    link = item.find('a').get('href')

    item_data = request.urlopen("{}{}".format(url, link)).read()
    item_bs = BeautifulSoup(item_data, 'lxml')

    author_link = item_bs.find('a', class_='l')
    author = author_link.text

    phone_button = item_bs.find('div', class_='phone')
    if not phone_button:
        continue

    phone_url = phone_button.find('a').get('onclick').split(',')[1].strip('\'')

    user_id = author_link.get('href').split('/')[-1]

    # inserting newly found user
    cur.execute('SELECT id FROM users WHERE id=? LIMIT 1', (user_id,))
    user_record = cur.fetchone()

    if user_record is None:
        cur.execute('INSERT INTO users VALUES(?, ?)',
                    (user_id, author))

    phone_data = request.urlopen("{}{}".format(url, phone_url)).read()
    phone_bs = BeautifulSoup(phone_data, 'lxml')

    phone_links = phone_bs.find('div', class_='phones').find_all('a')

    # numbers = []
    for phone_link in phone_links:
        # numbers.append(phone_link.text)
        cur.execute('INSERT INTO contacts (user_id, phone) VALUES (?, ?)',
                    (user_id, phone_link.text))

    post_id = link.split('/')[-1]
    post_descr = item_bs.find('div', class_='body').text

    cur.execute('SELECT id FROM posts WHERE id=? LIMIT 1', (post_id,))
    post_record = cur.fetchone()

    if post_record is None:
        cur.execute('INSERT INTO posts (id, user_id, title, descr) '
                    'VALUES (?, ?, ?, ?)',
                    (post_id, user_id, product.text, post_descr))

    conn.commit()

    # csv_writer.writerow((product.text, author, numbers, bool(hot)))

    print('Processed {} products'.format(idx))
