# Generated by Django 3.1.2 on 2020-10-21 08:31

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statistics", "0008_auto_20201021_1127"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hit",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime.utcnow, null=True
            ),
        ),
    ]
