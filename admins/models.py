from django.db import models
from .choices import CATEGORY_CHOICES, CATEGORY_COLORS

class Products(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    color = models.CharField(max_length=200, choices=CATEGORY_COLORS)
    price = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    stock = models.IntegerField()
    description = models.CharField(max_length=400)
    images = models.FileField()
    
    def __unicode__(self):
        return self.value