from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from scraping import get_products
from save_product import save_product,get_saved_products

# Va me permettre d'appeler directement par l'attribut dans le fichier html
class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

def search_products(request,search_product):
    (
        amazon_products,
        rdc_products,
        darty_products,
        fnac_products,
        rakuten_products,
    ) = get_products(search_product)
    
    return render(
        request,
        "home.html",
        {   
            "amazon_products": amazon_products[1],
            "amazon_best": objectview(amazon_products[0]),
            "rdc_products": rdc_products[1],
            "rdc_best": objectview(rdc_products[0]),
            "darty_products": darty_products[1],
            "darty_best": objectview(darty_products[0]),
            "fnac_products": fnac_products[1],
            "fnac_best": objectview(fnac_products[0]),
            "rakuten_products": rakuten_products[1],
            "rakuten_best": objectview(rakuten_products[0]),
        },   
    )

def render_page(request):
    saved_products_name = get_saved_products()
    return render(request, "home.html",{
        "saved_products": saved_products_name[0],
    })

def home(request):
    if request.method == "POST":
        data = request.POST.getlist('data')
        search_product = request.POST.get('product')
        if data != None:
            save_product(data)  
        if search_product != None:
            if search_product == "":
                return render_page(request)
            else:
                return search_products(request,search_product) 

    return render_page(request)
