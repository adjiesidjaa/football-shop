from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=60)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
