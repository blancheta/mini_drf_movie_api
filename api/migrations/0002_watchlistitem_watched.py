# Generated by Django 4.2.4 on 2024-06-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlistitem",
            name="watched",
            field=models.BooleanField(default=False),
        ),
    ]
