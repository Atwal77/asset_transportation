from django.db import models

class Rider(models.Model):
    name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    assets = models.PositiveIntegerField()

class Requester(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100, null=True)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    assets = models.PositiveIntegerField()

class TransportationRequest(models.Model):
    # Fields for the transportation request
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=20)
    num_assets = models.PositiveIntegerField()
    sensitivity = models.CharField(max_length=20)
    requester = models.ForeignKey('Requester', on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the model
        return f"{self.from_location} to {self.to_location}"