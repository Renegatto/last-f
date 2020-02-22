from django.contrib import admin
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def orders_list_page(request):
    return render(request, "order_list.html")

def order_page(request):
    return render(request, "order.html")