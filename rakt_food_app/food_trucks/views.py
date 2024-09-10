from django.contrib.gis.db.models.functions import Distance, Decimal
from django.contrib.gis.geos import Point
from food_trucks.models import FoodTruck
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import FoodTruckSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])
def nearby_food_trucks(request):
    """Return a list of nearby food trucks."""
    food_trucks = FoodTruck.objects.order_by(
        Distance(
            "location",
            Point(
                float(request.query_params["latitude"]),
                float(request.query_params["longitude"]),
                srid=4326,
            ),
        )
    )[:5]
    return Response({"food_trucks": FoodTruckSerializer(food_trucks, many=True).data})
