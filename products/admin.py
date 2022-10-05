from django.contrib import admin

from products.models import Category, Color, Product, SubCategory, Supplier

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Supplier)
admin.site.register(Color)