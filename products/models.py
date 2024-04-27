from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):  
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    item = models.CharField(max_length=255, null=False, blank=False, default='default_value_here')  # First line
    item_detail_1 = models.CharField(max_length=255, null=False, blank=True, default='default_value_here')  # Second line
    item_detail_2 = models.CharField(max_length=255, null=False, blank=True, default='default_value_here')  # Third line
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

