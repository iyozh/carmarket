# Generated by Django 3.1.2 on 2020-10-23 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0011_auto_20201023_1847"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="utm",
            name="link",
        ),
        migrations.DeleteModel(
            name="QRCode",
        ),
        migrations.DeleteModel(
            name="UTM",
        ),
    ]