from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "qty")
    search_fields = ("name",)

#  http://127.0.0.1:8000/api/products/  to see the products in the database
