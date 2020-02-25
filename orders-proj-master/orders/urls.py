from django.conf.urls import url
from django.urls import path, include
from orders import views
from orders.views import user_login, LoginView
from orders.viewsets import UsersViewSet, ProductsViewSet, OrderViewSet, CommentsViewSet

from rest_framework import routers

from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, 'users')
router.register(r'products', ProductsViewSet, 'products')
router.register(r'order', OrderViewSet, 'order')
router.register(r'comments', CommentsViewSet, 'comments')

urlpatterns = [
    path('', views.index),
    path('order', views.order_page, name='order_page'),
    path('orders_list', views.orders_list_page, name='orders'),

    url(r'^login', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    # path('login', user_login, name='login'),
    # path('login', user_login, name='login'),
    # path('login', LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('api/', include(router.urls)),
]
