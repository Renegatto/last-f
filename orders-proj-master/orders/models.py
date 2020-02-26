from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    user_type = models.CharField(max_length=2, default='test', choices=[
        ('MN', 'Manager'), ('CL', 'Client')], verbose_name='Пользователи')


class Products(models.Model):
    image = models.CharField(max_length=100, verbose_name='Изображение товара')
    description = models.TextField(
        blank=True, null=True, default=None, verbose_name='Описание товара')
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    price = models.CharField(max_length=100, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    products_list = models.ForeignKey(Products, on_delete=models.CASCADE)
    client = models.ForeignKey(Users, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, verbose_name='Автор')
    number = models.IntegerField()
    order_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Сумма заказа')
    order_comments = models.TextField(
        blank=True, null=True, default=None, verbose_name='Комментарий к заказу')
    order_status = models.CharField(max_length=50, choices=[('SN', 'Status new'), ('PK', 'Prepare kp'), ('KP', 'Kp'),
                                                            ('OR', 'Order'), ]
                                    )
    date_and_time_of_order = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='Создан')
    date_and_time_of_change_of_order = models.DateTimeField(
        auto_now_add=False, auto_now=True, verbose_name='Обновлён')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comments(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, primary_key=True)
    # author = models.ForeignKey(Users, on_delete=models.CASCADE)

    author = models.OneToOneField(
        Users, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True,
                            default=None, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class StatusOfOrder(models.Model):
    NEW = 'НОВЫЙ'
    PREP_KP = 'ПОДГОТОВКА_КП'
    KP = 'КП'
    ORDER = 'ЗАКАЗ'
    UNKNOWN = 'UNKNOWN'

    STATUS_CHOICES = (
        (NEW, 'НОВЫЙ'),
        (PREP_KP, 'ПОДГОТОВКА_КП'),
        (KP, 'КП'),
        (ORDER, 'ЗАКАЗ'),
        (UNKNOWN, 'UNKNOWN'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='UNKNOWN', editable=False)


    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



