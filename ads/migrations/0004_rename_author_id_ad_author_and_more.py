# Generated by Django 4.1 on 2022-08-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_rename_author_ad_author_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ad",
            old_name="author_id",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="ad",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="location_id",
            new_name="location",
        ),
    ]
