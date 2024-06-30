from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    item = models.CharField(max_length=255, default='default_value_here')
    item_detail_1 = models.CharField(max_length=255, blank=True, default='default_value_here')
    item_detail_2 = models.CharField(max_length=255, blank=True, default='default_value_here')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
