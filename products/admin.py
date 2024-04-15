from django.contrib import admin
from .models import Product, Category  # Update the import statement

# Register your models here.
class ProductAdmin(admin.ModelAdmin):  # Change the class name to ProductsAdmin
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'price',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)  # Register Products model with ProductsAdmin

