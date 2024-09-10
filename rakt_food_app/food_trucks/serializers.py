from rest_framework.serializers import ModelSerializer
from .models import FoodTruck


class FoodTruckSerializer(ModelSerializer):
    class Meta:
        model = FoodTruck
        exclude = ("location", "x_coordinate", "y_coordinate")
