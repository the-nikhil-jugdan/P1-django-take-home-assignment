# Generated by Django 5.1.1 on 2024-09-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_trucks', '0003_alter_foodtruck_x_coordinate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='prior_permit',
            field=models.IntegerField(null=True),
        ),
    ]
