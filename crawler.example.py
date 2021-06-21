#pip install beautifulsoup4
#1
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Stock/index.html'
reqs = requests.get(url)
html_doc = reqs.text

soup = BeautifulSoup(html_doc, 'html.parser')
text = soup.get_text()
#print('html:', html_doc)
#print(soup.title.string )

#titles = soup.find('div', class_ = 'title')
#print(titles.a.string)

titles = soup.find_all('div', class_ = 'title')
for i in titles:
    if i.a != None:
        print(i.a.string)
'''
#test
'''
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/p/pl?d=graphic+cards'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup =  soup(page_html, 'html.parser')
print(page_soup.h1)
'''

#2 google
'''
import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.google.com/')
#print(result.status_code)
#print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')
#print(links)
for link in links:
    if '關於' in link.text:
        print(link)
        print(link.attrs['href'])
'''
#3 whitehouse briefing 
'''
import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.whitehouse.gov/briefing-room/')
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []

for h2 in soup.find_all('h2'):
    a = h2.find('a')
#try-except to avoid Nonetype
    try:
        if 'href' in a.attrs:
            urls.append(a.attrs['href'])
    except:
        pass 
print(urls)
'''
#4










