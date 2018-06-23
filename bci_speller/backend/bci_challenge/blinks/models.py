from django.db import models


class BCIDevice(models.Model):
    device_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return device_id
