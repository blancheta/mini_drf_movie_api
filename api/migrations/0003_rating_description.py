# Generated by Django 4.2.4 on 2024-06-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_watchlistitem_watched"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
