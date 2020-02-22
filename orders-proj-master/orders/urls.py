from django.urls import path, include
from orders import views
from orders.viewsets import UsersViewSet, ProductsViewSet, OrderViewSet, CommentsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, 'users')
router.register(r'products', ProductsViewSet, 'products')
router.register(r'order', OrderViewSet, 'order')
router.register(r'comments', CommentsViewSet, 'comments')

urlpatterns = [
    path('', views.index),
    path('order', views.order_page),
    path('orders_list', views.orders_list_page),

    path('api/', include(router.urls)),
]
