# Generated by Django 4.2.2 on 2023-06-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("beta_product", "0002_userinterest_unique_identifier_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinterest",
            name="unique_identifier",
            field=models.CharField(
                blank=True, default=None, max_length=100, null=True, unique=True
            ),
        ),
    ]