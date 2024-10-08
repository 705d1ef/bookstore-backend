# Generated by Django 4.2.1 on 2023-06-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_book_options_alter_book_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(
                blank=True,
                help_text="The image of book",
                upload_to="",
                verbose_name="Cover",
            ),
        ),
    ]
