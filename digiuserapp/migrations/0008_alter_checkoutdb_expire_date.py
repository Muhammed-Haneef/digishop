# Generated by Django 4.1.7 on 2023-06-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiuserapp', '0007_checkoutdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdb',
            name='Expire_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
