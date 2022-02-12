from django.db import models


class Wheather(models.Model):
    city = models.CharField(max_length=200)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
