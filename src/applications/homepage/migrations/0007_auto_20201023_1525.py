# Generated by Django 3.1.2 on 2020-10-23 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0006_auto_20201023_1514"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qrcode",
            name="link",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="homepage.link"
            ),
        ),
    ]
