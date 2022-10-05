from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(unique=True, max_length=200)
    phone_num = models.CharField(unique=True, max_length=12)
class Product(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=400)
    price = models.FloatField(max_length=200, default=0.00)
    suplier = models.ForeignKey(to=Supplier, null=True, on_delete=models.CASCADE)

class Color(models.Model):
    name = models.CharField(unique=True, max_length=30, null=False)
    color_value = models.CharField(max_length=10, null=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.CharField(null=True, max_length=300)

class SubCategory(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = models.CharField(null=True, max_length=300)
    parent = models.ForeignKey(to=Category, null=True, on_delete=models.DO_NOTHING)
