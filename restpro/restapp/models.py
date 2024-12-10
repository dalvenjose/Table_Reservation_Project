from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='biriyani')  # Changed TextField to CharField
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)