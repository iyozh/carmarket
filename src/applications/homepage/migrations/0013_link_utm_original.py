# Generated by Django 3.1.2 on 2020-10-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0012_auto_20201023_2003"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="utm_original",
            field=models.URLField(blank=True, null=True),
        ),
    ]
