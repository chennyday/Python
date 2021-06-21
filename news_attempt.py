#bbc

import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news/world'
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'html.parser')
#class="gs-c-promo-body
articles = soup.find_all('div', class_ = 'gs-c-promo-body')
#articles = soup.find_all('div', class_ = 'gs-c-promo')
i = 0
for article in articles:
    i = i + 1
    print(i)
    print('Article:')
    headline = article.find('h3')
    print(headline.text)
    link = article.find('a')
#fix url
    print(link['href'])
    #summary = article.find('p')
    summary = article.find('p', class_ = 'gs-c-promo-summary')
    if summary != None:
        print('summary:', summary.text)
    #print(article)
    print()

print('*******************')    
summaries = soup.find_all('p', class_ = 'gs-c-promo-summary')
for summary in summaries:
    print(summary.text)


#cnn
'''
import requests
from bs4 import BeautifulSoup

result = requests.get('https://edition.cnn.com/')
src = result.content
soup = BeautifulSoup(src, 'html.parser')

articles = soup.find_all('div', class_ = 'cd__content')
for article in articles:
    print('Article:')
    headline = article.find('span')
    print(headline.text)
    link = article.find('a')
    print(link['href'])
'''
    
    
    
    
    
    
    