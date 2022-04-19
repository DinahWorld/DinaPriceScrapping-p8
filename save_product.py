import csv  
from datetime import datetime
import collections
from math import prod

# Je crée un fichier csv avec les données du produit
def save_product(products):
    now = datetime.now()
    dt_string = now.strftime("@%d/%m/%Y@%H:%M:%S")
    for product in products:
        product = str(product) + dt_string
        product = product.split("@")
        print(product)
        name = product[0].replace(" ", "_")
        with open('data/'+name+'.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([product])


def get_product():
    with open('best_prices.csv', 'r', encoding='UTF8') as f:
        my_reader = csv.DictReader(f)
        first_row = next(my_reader)
        for row in my_reader:
            print (row['name'])


get_product()