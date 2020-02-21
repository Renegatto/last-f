from django.contrib import admin

from orders.models import Users, Products, Order, Comments

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Comments)
