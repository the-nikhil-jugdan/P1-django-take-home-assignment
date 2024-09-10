from django.contrib.gis.db import models
from .choices import StatusChoices


# Create your models here.
class FoodTruck(models.Model):
    name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=50)

    cnn = models.CharField(max_length=20)
    description = models.TextField()
    address = models.TextField()
    block_lot = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    lot = models.CharField(max_length=20)
    permit = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)
    food_items = models.TextField()
    x_coordinate = models.DecimalField(max_digits=30, decimal_places=15, null=True)
    y_coordinate = models.DecimalField(max_digits=30, decimal_places=15, null=True)

    schedule = models.URLField(max_length=500)
    days_hours = models.CharField(max_length=100)
    approved_date = models.DateField()
    received_date = models.DateField()
    expiration_date = models.DateField()

    prior_permit = models.IntegerField(null=True)

    location = models.PointField()
    location_id = models.BigIntegerField(unique=True)

    fire_prevention_district = models.CharField(max_length=6)
    police_district = models.CharField(max_length=6)
    supervisor_district = models.CharField(max_length=6)
    zip_code = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=6)
