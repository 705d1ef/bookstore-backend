# Generated by Django 4.2.1 on 2023-06-06 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0002_alter_book_options_book_author_book_cover_book_genre_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Book", "verbose_name_plural": "Books"},
        ),
        migrations.AlterField(
            model_name="book",
            name="number_of_pages",
            field=models.CharField(
                blank=True, null=True, verbose_name="Number of pages"
            ),
        ),
    ]
