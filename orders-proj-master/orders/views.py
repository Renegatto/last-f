from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from orders.forms import LoginForm

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from orders.models import Order, Users

from django.contrib.auth.decorators import login_required
from orders.forms import OrderForm

def index(request):
    return render(request, "index.html")


@login_required
def orders_list_page(request):
    data = {'Orders': Order.objects.all(
    ), 'Users': Users.objects.filter(user_type='MN')}

    return render(request, "order_list.html", context=data)


# доделать тут!
@login_required
def order_page(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.id = request.id
        order.author = request.author
        order.number = request.number
        order.order_price = request.order_price
        order.order_comments = request.order_comments
        order.date_and_time_of_order = timezone.now()
        order.order_status = request.order_status
        order.products_list = request.products_list
        order.client = request.client
        order.save()
    return render(request, "order.html",  {'form': form})


@csrf_exempt
def user_login(request):
    userform = LoginForm()
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            return redirect('orders')
    return render(request, "registration/login.html", {"form": userform})
