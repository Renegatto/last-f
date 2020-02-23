# Generated by Django 3.0.2 on 2020-02-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200223_1504'),
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
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('MN', 'Manager'), ('CL', 'Client')], default='test', max_length=2),
        ),
    ]