from itertools import product
from django.db import models

from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()



class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    # def __str__(self):
    #     return {self.author} {self.product}