# Generated by Django 4.1.7 on 2023-06-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiuserapp', '0004_cartdb_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='cartimg'),
        ),
    ]
