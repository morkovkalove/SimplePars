import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3




url = 'https://www.roscosmos.ru/102/'

r = requests.get(url)
r.text
soup = BeautifulSoup(r.text, 'lxml')


link = soup.find('div', class_= 'centercolumn').findAll('span', class_= 'name')

links = []

for i in link:
    links.append(i.string)
    sleep(1)
    print(i.text)


conn = sqlite3.connect("titles.db")

cursor = conn.cursor()

cursor.executemany("INSERT INTO titles VALUES(?)", links)

conn.commit()
conn.close()