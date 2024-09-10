from django.core.management import BaseCommand
import pandas as pd
from food_trucks.models import FoodTruck
import os
import datetime
from django.contrib.gis.geos import Point
from decimal import Decimal
import numpy as np

dTypes = {
    "Address": "string",
    "Applicant": "string",
    "Approved": "string",
    "ExpirationDate": "string",
    "FacilityType": "string",
    "Fire Prevention Districts": "string",
    "FoodItems": "string",
    "Latitude": "string",
    "Location": "string",
    "LocationDescription": "string",
    "Longitude": "string",
    "NOISent": "string",
    "Neighborhoods (old)": "string",
    "Police Districts": "string",
    "PriorPermit": "int32",
    "Received": "string",
    "Schedule": "string",
    "Status": "string",
    "Supervisor Districts": "string",
    "X": "float64",
    "Y": "float64",
    "Zip Codes": "string",
    "block": "string",
    "blocklot": "string",
    "cnn": "string",
    "dayshours": "string",
    "locationid": "int64",
    "lot": "string",
    "permit": "string",
}


class Command(BaseCommand):
    help = "Load data from the given file"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **kwargs):
        file = kwargs["file"]
        data = pd.read_csv(f"{os.getcwd()}/{file}", dtype=dTypes)
        data["X"].fillna(-1, inplace=True)
        data["Y"].fillna(-1, inplace=True)
        for index, row in data.iterrows():
            FoodTruck.objects.update_or_create(
                location_id=row["locationid"],
                defaults={
                    "name": row["Applicant"],
                    "facility_type": row["FacilityType"],
                    "cnn": row["cnn"],
                    "description": row["LocationDescription"],
                    "address": row["Address"],
                    "block_lot": row["blocklot"],
                    "block": row["block"],
                    "lot": row["lot"],
                    "permit": row["permit"],
                    "status": row["Status"],
                    "food_items": row["FoodItems"],
                    "schedule": row["Schedule"],
                    "days_hours": row["dayshours"],
                    "prior_permit": row["PriorPermit"],
                    "fire_prevention_district": row["Fire Prevention Districts"],
                    "police_district": row["Police Districts"],
                    "supervisor_district": row["Supervisor Districts"],
                    "zip_code": row["Zip Codes"],
                    "neighborhood": row["Neighborhoods (old)"],
                    "location": Point(
                        (Decimal(row["Latitude"]), Decimal(row["Longitude"])), srid=4326
                    ),
                    "x_coordinate": None if row["X"] == -1 else Decimal(row["X"]),
                    "y_coordinate": None if row["Y"] == -1 else Decimal(row["Y"]),
                },
                create_defaults={
                    "approved_date": datetime.datetime.now(),
                    "received_date": datetime.datetime.now(),
                    "expiration_date": datetime.datetime.now(),
                    "location": Point(
                        (Decimal(row["Latitude"]), Decimal(row["Longitude"])), srid=4326
                    ),
                },
                # TODO: Improve Data reading into DB
            )
