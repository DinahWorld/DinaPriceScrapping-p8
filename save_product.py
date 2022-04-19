import csv  
from datetime import datetime
import glob

# Je crée un fichier csv avec les données du produit
def save_product(products):
    # Je récupere la date et le temps actuel
    now = datetime.now()
    dt_string = now.strftime("@%d/%m/%Y@%H:%M:%S")
    for product in products:
        product = str(product) + dt_string
        product = product.split("@")
        name = product[0].replace(" ", "_").replace("-", "_").replace("/", "_").replace(",", "_").replace(".", "_")
        with open('data/'+name+'.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([product])

# Je récupere les produits des fichiers csv
def get_saved_products():
    data = []
    data_files = glob.glob("./data/*.csv")
    print(data_files)
    for data_file in data_files:
        with open(str(data_file), 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
                print(row)
    return data