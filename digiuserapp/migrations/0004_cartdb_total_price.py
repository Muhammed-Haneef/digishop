# Generated by Django 4.1.7 on 2023-06-12 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiuserapp', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]