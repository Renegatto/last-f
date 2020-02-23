from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from orders.forms import LoginForm

from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect


from orders.models import Order, Users


def index(request):
    return render(request, "index.html")


def orders_list_page(request):
    data = {'Orders': Order.objects.all(
    ), 'Users': Users.objects.filter(user_type='MN')}

    return render(request, "order_list.html", context=data)


def order_page(request):
    return render(request, "order.html")


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('http://localhost:8000/orders_list')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
