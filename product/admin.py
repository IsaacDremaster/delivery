from django.contrib import admin
from .models import Products, ProductImage, ProductMark


admin.site.register(Products)
admin.site.register(ProductMark)
admin.site.register(ProductImage)