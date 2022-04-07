from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from scraping import get_products


def home(request):
    if request.method == "POST":
        search_product = request.POST.get("product")
        (
            amazon_products,
            rdc_products,
            darty_products,
            fnac_products,
            rakuten_products,
        ) = get_products(search_product)
        print(amazon_products[0])
        return render(
            request,
            "home.html",
            {   
                "amazon_products": amazon_products[1],
                "amazon_best_product": amazon_products[0]['name'],
                "amazon_best_price": amazon_products[0]['price'],
                "amazon_best_url": amazon_products[0]['url'],
                "rdc_products": rdc_products[1],
                "rdc_best_product": rdc_products[0]['name'],
                "rdc_best_price": rdc_products[0]['price'],
                "rdc_best_url": rdc_products[0]['url'],
                "darty_products": darty_products[1],
                "darty_best_product": darty_products[0]['name'],
                "darty_best_price": darty_products[0]['price'],
                "darty_best_url": darty_products[0]['url'],
                "fnac_products": fnac_products[1],
                "fnac_best_product": fnac_products[0]['name'],
                "fnac_best_price": fnac_products[0]['price'],
                "fnac_best_url": fnac_products[0]['url'],
                "rakuten_products": rakuten_products[1],
                "rakuten_best_product": rakuten_products[0]['name'],
                "rakuten_best_price": rakuten_products[0]['price'],
                "rakuten_best_url": rakuten_products[0]['url'],
            },   
        )
    else:
        return render(request, "home.html")


urlpatterns = [
    path("", home),
]
