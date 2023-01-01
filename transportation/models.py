from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    assets = models.PositiveIntegerField()

class Requester(models.Model):
    name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    assets = models.PositiveIntegerField()
