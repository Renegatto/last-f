# Generated by Django 3.0.2 on 2020-02-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200223_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='client',
        ),
        migrations.RemoveField(
            model_name='users',
            name='manager',
        ),
    ]