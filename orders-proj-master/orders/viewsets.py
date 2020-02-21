from orders.models import Users, Products, Order, Comments
from orders.serializers import UsersSerializer, ProductsSerializer, OrderSerializer, CommentsSerializer
from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        serializer_class = UsersSerializer


class ProductsViewSet(viewsets.ModelViewSet):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many= True)
        serializer_class = ProductsSerializer


class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many= True)
        serializer_class = OrderSerializer


class CommentsViewSet(viewsets.ModelViewSet):
        queryset = Comments.objects.all()
        serializer = CommentsSerializer(queryset, many=True)
        serializer_class = CommentsSerializer
