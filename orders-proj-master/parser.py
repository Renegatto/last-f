import requests
from bs4 import BeautifulSoup

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django

django.setup()

from orders.models import Products

products = []
product = {}

elems = soup.find("div", {'class': 'prod'})

for elem in elems:
    product['image']  = elem.find("картинка")
    product['name']  = elem.find("заголовк")
    product['price']  = elem.find("цена")
    products.append(product)

def get_soup():
    URL = 'https://home.1k.by/kitchen-coffeemakers/'
    r = requests.get(URL)
    return r.text


soup = BeautifulSoup(get_soup(), "lxml")
names = soup.findAll("a", {"class": "prod__link"})
descriptions = soup.find("div", {"class": 'l-columns__main'}).findAll('p')
pics = soup.findAll("img", {"class": "prod__img"})
price = soup.findAll("span", {"class": "money money--cash"})

# data
list_of_names = [n.get_text() for n in names]
list_of_descriptions = [d.get_text() for d in descriptions]
list_of_pics = [p['src'] for p in pics]
list_of_price = [c.get_text() for c in price]

for p in products:
    pr = Products.objects.create()
    pr.description = p['desc']
    pr.image = p['image']
    pr.description = p['description']
    pr.save()

#
# # add data to fields Products table
# for n in list_of_names:
#     add_name = Products.objects.create(name = n)
#
# for d in list_of_descriptions:
#     add_desk = Products.objects.create(description = d)
#
# for p in list_of_pics:
#     add_pick = Products.objects.create(image = p)
#
# for pr in list_of_price:
#     add_price = Products.objects.create(price = pr)


# p = Products.objects.all().delete
print(p)
#
