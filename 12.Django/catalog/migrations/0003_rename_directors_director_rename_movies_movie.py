# Generated by Django 4.1 on 2022-08-20 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_directors_name_directors_first_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Directors',
            new_name='Director',
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
