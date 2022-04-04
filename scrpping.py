import requests
from bs4 import BeautifulSoup

# Idée : Récuperer les liens des sites commercants qui vendent x produit
# Ce que je vais faire : Je récupere le prix de gros sites marchant

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

product = 'rtx'
URL = 'https://www.amazon.fr/s?k='+ product + '&page=0'

#items = []
#response = requests.get(URL + '&page=0', headers=headers)
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
for result in results:
    product_name = result.h2.text
    try:
        rating = result.find('i', {'class': 'a-icon'}).text
        #rating_count = result.find_all('span', {'aria-label': True})[1].text
    except AttributeError:
        continue
    try:
        price = result.find('span', {'class': 'a-price-whole'}).text
     
        #print(product_name,price)
        #product_url = 'https://amazon.fr' + result.h2.a['href']
        print(price)
        #items.append([product_name, rating, rating_count, price, product_url])
    except AttributeError:
        continue
    
