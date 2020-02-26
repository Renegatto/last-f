from orders.models import Products
import django
from bs4 import BeautifulSoup
import requests
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
    product['image'] = elem.find("img", {'class': 'prod__img'})['src']
    product['name'] = elem.find("header", {'class': 'prod__head'}).get_text()
    product['price'] = elem.find("a", {'class': 'money__val'}).get_text()
    product['description'] = elem.find(
        "p", {'class': 'prod__descr'}).get_text()
    products.append(product)


for p in products:
    pr = Products.objects.create()
    pr.name = product['name']
    pr.image = product['image']
    pr.description = product['description']
    pr.price = product['price']
    pr.save()
