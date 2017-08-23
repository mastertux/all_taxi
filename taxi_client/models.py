from django.db import models

class TaxiClient(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )