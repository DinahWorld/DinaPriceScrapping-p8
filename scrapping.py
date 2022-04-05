import requests
from bs4 import BeautifulSoup

# Idée : Récuperer les liens des sites commercants qui vendent x product
# Ce que je vais faire : Je récupere le prix de gros sites marchant
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

#items = []
#response = requests.get(URL + '&page=0', headers=headers)

def get_amazon_price(product):
    url = 'https://www.amazon.fr/s?k='+ product + '&page=0'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    product = []
    for result in results:
        try:
            product_name = result.h2.text
            price = result.find('span', {'class': 'a-price-whole'}).text
            product_url = 'https://amazon.fr' + result.h2.a['href']
            product.append(
                {'name' : product_name, 'price': price, 'url' : product_url})
        except AttributeError:
            continue

    return product
    
def get_rdc_price(product):
    url = 'https://www.rueducommerce.fr/r/'+ product + '.html'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('article')
    product = []

    for result in results:
        try:
            product_name = result.h2.text
            product_name = " ".join(product_name.split())
            price = result.find('span', {'class': 'item__price--new-box'}).text
            price = " ".join(price.split()).replace('€','').replace(' ','').replace(',','.')
            try:
                price_float = float(price)
                product_url = 'https://www.rueducommerce.fr' + result.h2.a['href']
                product.append(
                {'name' : product_name, 'price': price, 'url' : product_url})
            except ValueError:
                continue
        except AttributeError:
            continue
    
    return product

def get_cdiscount_price(product):
    url = 'https://www.cdiscount.com/search/10/'+ product + '.html'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('li')
    product = []
    for result in results:
        try:
            product_name = result.find('div', {'class': 'prdtBILTit'}).text
            print(product_name)

        except AttributeError:
            continue

get_cdiscount_price('nvidia rtx')