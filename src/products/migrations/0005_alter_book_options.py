# Generated by Django 4.2.1 on 2023-06-17 00:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_remove_book_size_book_description_book_dimensions_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name_plural": "Authors"},
        ),
    ]
