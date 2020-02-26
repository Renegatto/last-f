from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from orders.models import Users, Products, Order, Comments

admin.site.register(Users, UserAdmin)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Comments)
