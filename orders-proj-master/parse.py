

import django
from orders.models import Products

import requests
from bs4 import BeautifulSoup

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

products = []
product = {}


def get_soup():
    URL = 'https://home.1k.by/kitchen-coffeemakers/'
    r = requests.get(URL)
    return r.text


soup = BeautifulSoup(get_soup(), 'html.parser')
elems = soup.find_all("div", {'class': 'prod prod--toggle'})


for elem in elems:
    product = {
        'image': elem.find_next("img", {'class': 'prod__img'})['src'],
        'name': elem.find_next("header", {'class': 'prod__head'}).get_text(),
        'price': elem.find_next("a", {'class': 'money__val'}).get_text(),
        'description': elem.find_next(
            "p", {'class': 'prod__descr'}).get_text()
    }
    products.append(product)

    # for product in products:
    #     pr = Products.objects.create()
    #     pr.name = product['name']
    #     pr.image = product['image']
    #     pr.description = product['description']
    #     pr.price = product['price']
    #     pr.save()


for x in products[0:10]:
    for item in x.items():
        print(item)
