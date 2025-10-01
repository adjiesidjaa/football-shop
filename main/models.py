from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('JER', 'Jersey'),
        ('SEP', 'Sepatu Bola'),
        ('BOL', 'Bola'),
        ('LAT', 'Peralatan Latihan'),
        ('AKS', 'Aksesoris'),
        ('MER', 'Merchandise Klub'),
        ('OTH', 'Lainnya'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(
        max_length=60,
        choices=CATEGORY_CHOICES,
        default='OTH'
    )
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
