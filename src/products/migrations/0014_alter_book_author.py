# Generated by Django 4.2.1 on 2023-08-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0013_remove_book_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=255, verbose_name="Author"),
        ),
    ]
