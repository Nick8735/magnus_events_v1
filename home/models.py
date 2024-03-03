from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False)  # Add this line

    def __str__(self):
        return self.name