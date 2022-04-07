from math import prod
import requests
from bs4 import BeautifulSoup

# Idée : Récuperer les liens des sites commercants qui vendent x product
# Ce que je vais faire : Je récupere le prix de gros sites marchant
# Récuperer l'image du produit
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}

def get_products(product):
    amazon_products = get_amazon_products(product)
    rdc_products = get_rdc_products(product)
    darty_products = get_darty_products(product)
    fnac_products = get_fnac_products(product)
    rakuten_products = get_rakuten_products(product)
    return (amazon_products, rdc_products, darty_products,fnac_products,rakuten_products)

def get_amazon_products(product):
    product = product.replace(' ', '+')
    url = 'https://www.amazon.fr/s?k='+ product + '&page=0'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(
        "div", {"class": "s-result-item", "data-component-type": "s-search-result"}
    )
    print('Amazon ',response)
    products = []
    best_price = []
    i = 0
    for result in results:
        if i == 5:
            break
        try:
            product_name = result.h2.text
            price = result.find('span', {'class': 'a-price-whole'}).text
            product_url = 'https://amazon.fr' + result.h2.a['href']
            i += 1
            try:
                price = price.replace(',', '.')
                price = float(price)
                products.append({'name' : product_name, 'price': price, 'url' : product_url})  
            except ValueError:
                    continue
        except AttributeError:
            continue
    
    try:
        best_price = min(products, key=lambda x:x['price'])
        best_price['price'] = '{0}€'.format(best_price['price'])
    except ValueError:
        return [best_price, products]
    return [best_price, products]
    
def get_rdc_products(product):
    product = product.replace(' ', '-')
    url = 'https://www.rueducommerce.fr/r/'+ product + '.html'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('article')
    products = []
    best_price = []
    print('Rue Du Commerce ',response)
    i = 0
    for result in results:
        if i == 5:
            break
        try:
            product_name = result.h2.text
            product_name = " ".join(product_name.split())
            price = result.find('span', {'class': 'item__price--new-box'}).text
            price = " ".join(price.split()).replace('€','').replace(' ','').replace(',','.')
            product_url = 'https://www.rueducommerce.fr' + result.h2.a['href']
            i += 1
            try:
                price = float(price)
                products.append({'name' : product_name, 'price': price, 'url' : product_url})  
            except ValueError:
                continue
        except AttributeError:
            continue
    try:
        best_price = min(products, key=lambda x:x['price'])
        best_price['price'] = '{0}€'.format(best_price['price'])
    except ValueError:
        best_price ={'name' : 'Indisponible', 'price': 'Indisponible', 'url' : 'Indisponible'}

    return [best_price, products]


def get_darty_products(product):
    product = product.replace(' ', '-')
    url = 'https://www.darty.com/nav/recherche/'+ product + '.html'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'product_detail next_prev_info'})
    products = []
    best_price = []
    print('Darty ',response)
    i = 0
    for result in results:
        if i == 5:
            break
        try:
            product_name = result.find('span', {'class': 'prd-name'}).text
            price = result.find('div', {'class': 'product-price__price'}).text
            price = " ".join(price.split()).replace('€','').replace('*','').replace(' ','').replace(',','.')
            product_url = 'https://www.darty.com' + result.a['href']
            i += 1
            try:
                price = price.replace(',', '.')
                price = float(price)
                products.append({'name' : product_name, 'price': price, 'url' : product_url})
            except ValueError:
                    continue
        except AttributeError:
            continue
    try:
        best_price = min(products, key=lambda x:x['price'])
        best_price['price'] = '{0}€'.format(best_price['price'])
    except ValueError:
        best_price ={'name' : 'Indisponible', 'price': 'Indisponible', 'url' : 'Indisponible'}
    return [best_price, products]

def get_fnac_products(product):
    product = product.replace(' ', '+')
    url = 'https://www.fnac.com/SearchResult/ResultList.aspx?SCat=0&Search='+ product + '&sft=1&sa=0'
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'clearfix Article-item js-Search-hashLinkId'})
    products = []
    best_price = []
    print('Fnac ',response)
    i = 0
    for result in results:
        if i == 5:
            break
        try:
            product_name = result.find('a', {'class': 'Article-title js-Search-hashLink'}).text
            price = result.find('strong', {'class': 'userPrice'}).text
            price = " ".join(price.split()).replace('*','').replace(' ','').replace(',','.')
            product_url = result.a['href']
            i += 1
            try:
                price = price.replace('€', '.')
                price = float(price)
                products.append({'name' : product_name, 'price': price, 'url' : product_url}) 
            except ValueError:
                    continue
        except AttributeError:
            continue

    try:
        best_price = min(products, key=lambda x:x['price'])
        best_price['price'] = '{0}€'.format(best_price['price'])
    except ValueError:
        best_price ={'name' : 'Indisponible', 'price': 'Indisponible', 'url' : 'Indisponible'}
    return [best_price, products]
    
def get_rakuten_products(product):
    product = product.replace(' ', '+')
    url = 'https://fr.shopping.rakuten.com/search/'+ product
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'pt-16 br bb productList_borderColor_2W- pb-24 flex productList_gridCard_15h'})
    products = []
    best_price = []
    print('Rakuten ',response)
    i = 0
    for result in results:
        if i == 5:
            break
        try:
            product_name = result.find('div', {'class': 'di'}).p.text
            price = result.find('div', {'class': 'pt-16'}).span.text
            price = " ".join(price.split()).replace('*','').replace(' ','').replace(',','.')
            i += 1
            price = price.replace('€', ' ')
            price = float(price)
            product_url = 'https://fr.shopping.rakuten.com' + result.a['href']   
            products.append({'name' : product_name, 'price': price, 'url' : product_url})
        except AttributeError:
            continue
        except ValueError:
                continue

    try:
        best_price = min(products, key=lambda x:x['price'])
        best_price['price'] = '{0}€'.format(best_price['price'])
    except ValueError:
        best_price ={'name' : 'Indisponible', 'price': 'Indisponible', 'url' : 'Indisponible'}
    return [best_price, products]
