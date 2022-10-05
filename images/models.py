from django.db import models

from products.models import Product

# Create your models here.

class Images(models.Model):
    url = models.CharField(max_length=500, null=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)