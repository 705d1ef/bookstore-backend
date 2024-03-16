# Generated by Django 4.2.1 on 2024-03-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_alter_book_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="quantity",
            field=models.PositiveSmallIntegerField(blank=True, verbose_name="In stock"),
        ),
    ]
