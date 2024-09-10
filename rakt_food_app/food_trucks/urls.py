from django.urls import path

from .views import nearby_food_trucks

urlpatterns = [
    path("nearby-food-trucks/", nearby_food_trucks, name="nearby-food-trucks"),
]
