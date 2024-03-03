from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)  # Adjusted max_length for description field
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


    def __str__(self):
        return self.name

    