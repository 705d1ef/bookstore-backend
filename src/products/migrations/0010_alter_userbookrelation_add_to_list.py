# Generated by Django 4.2.1 on 2023-06-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_book_rating_userbookrelation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userbookrelation",
            name="add_to_list",
            field=models.BooleanField(default=False, verbose_name="Add to List"),
        ),
    ]
