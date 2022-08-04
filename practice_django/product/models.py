from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    categories = models.ManyToManyField(Category, related_name='products')
    