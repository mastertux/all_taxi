from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_driver.models import TaxiDriver
from taxi_client.models import TaxiClient

class User(AbstractUser):
    driver = models.ForeignKey(
        TaxiDriver,
        null=True,
        blank=True
    )

    client = models.ForeignKey(
        TaxiClient,
        null=False,
        blank=False
    )
