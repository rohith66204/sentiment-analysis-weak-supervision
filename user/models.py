from django.db import models
from django.conf import settings
from admins.models import Products

class Orders(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    prod = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    # prod = models.ForeignKey(Products)
    prodqty = models.IntegerField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=10,default="pending")
    dateordered = models.DateField(auto_now=True)
        
class Ratings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    # product = models.ForeignKey(Products)
    ratings = models.IntegerField()
    reviews = models.CharField(max_length=200)
    sentiments = models.CharField(max_length=200)
