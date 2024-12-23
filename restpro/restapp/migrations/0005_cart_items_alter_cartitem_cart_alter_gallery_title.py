# Generated by Django 5.1.3 on 2024-12-09 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='restapp.CartItem', to='restapp.menu'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='restapp.cart'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='biriyani', max_length=100),
        ),
    ]
