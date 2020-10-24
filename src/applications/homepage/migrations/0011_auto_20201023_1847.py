# Generated by Django 3.1.2 on 2020-10-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0010_utm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="utm",
            name="utm_campaign",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_content",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_medium",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_source",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="utm",
            name="utm_term",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]