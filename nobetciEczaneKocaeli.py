import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://www.kocaelieo.org.tr/"

htmlData = rq.get(url).content
soupData = bs(htmlData, 'html.parser')


list = soupData.find_all('div', {'class': ['panel-body']})
liste = []

for x in list:
    pharmacyName = x.span.text.strip()
    pharmacyPhoneNumber = x.find('a',{'class':['gri']}).get('href').replace('tel','').replace(':','')
    pharmacyGoogleMapLink = x.find('a',{'class':['red']}).get('href')
    liste.append(x.p.text.strip().replace('\n','').replace('             ',' ').replace(' Navigasyona Git!','').split('ECZANESİ'))

for i in liste:
    print(f"Eczane Adı: {i[0]} Eczanesi - İletişim: {i[1]}")


