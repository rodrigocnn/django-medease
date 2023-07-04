from django.db import models


class Service(models.Model):
    description = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
