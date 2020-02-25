from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from orders.forms import LoginForm

from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from orders.models import Order, Users

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


@login_required
def orders_list_page(request):
    data = {'Orders': Order.objects.all(
    ), 'Users': Users.objects.filter(user_type='MN')}

    return render(request, "order_list.html", context=data)


@login_required
def order_page(request):
    return render(request, "order.html")


@csrf_exempt
def user_login(request):
    userform = LoginForm()
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            return redirect('order_page')
            # return render(request, "order.html", {"form": userform})
    return render(request, "registration/login.html", {"form": userform})
