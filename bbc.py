#1 news
'''
import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.bbc.com/news')
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
links = soup.find_all('a', class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
for link in links:
    urls.append(link.attrs['href'])
print(urls)
print()

titles = soup.find_all('div', class_ = 'gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m')
for title in titles:
    if title.a != None:
        print(title.a.string)
'''
#2 world news
'''
import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.bbc.com/news/world')
scrc = result.content
soup = BeautifulSoup(src, 'lxml')

for h3 in soup.find_all('h3'):
    print(h3.text)
'''