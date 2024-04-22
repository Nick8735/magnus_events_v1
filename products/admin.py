from django.contrib import admin
from django.utils.safestring import mark_safe  # Add this import
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'price',
        'display_image',
    )

    ordering = ('sku',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" style="max-width:100px; max-height:100px;"/>'.format(obj.image.url))
        else:
            return 'No Image'

    display_image.allow_tags = True
    display_image.short_description = 'Image'

# Register only the Product model in the admin interface
admin.site.register(Product, ProductAdmin)
