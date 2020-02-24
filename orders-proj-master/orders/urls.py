from django.urls import path, include
from orders import views
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
    path('order', views.order_page),
    path('orders_list', views.orders_list_page, name='orders'),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('api/', include(router.urls)),
]
