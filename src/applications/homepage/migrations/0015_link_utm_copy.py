# Generated by Django 3.1.2 on 2020-10-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0014_remove_link_utm_original"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="utm_copy",
            field=models.URLField(blank=True, null=True),
        ),
    ]
