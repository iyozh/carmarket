# Generated by Django 3.1.3 on 2020-11-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statistics", "0013_auto_20201101_2050"),
    ]

    operations = [
        migrations.AlterField(
            model_name="utm",
            name="utm_campaign",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_content",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_medium",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_source",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_term",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
