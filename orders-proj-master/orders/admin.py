from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #добавить в регистр к юзеру, чтобы логиниться не только от админа
from django.forms import forms

from orders.models import Users, Products, Order, Comments
from django import forms


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['user_type'].queryset = Users.objects.filter(user_type='CL')


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm


admin.site.register(Users, ClientAdmin)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Comments)

