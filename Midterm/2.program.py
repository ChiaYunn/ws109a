import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
rank, pg, rat = [], [], []
url = 'https://www.tiobe.com/tiobe-index/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
datas = sp.find('table', id='top20')
rows = datas.select('tbody tr')
for row in rows:
    cols = row.select('td')
    rank.append(int(cols[0].text))
    pg.append(str(cols[3].text))
    rat.append(str(cols[4].text))
print(rank)
print(pg)
print(rat)
