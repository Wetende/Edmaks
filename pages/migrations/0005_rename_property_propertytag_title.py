# Generated by Django 4.0.6 on 2023-02-10 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_propertytag_property_delete_property'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertytag',
            old_name='property',
            new_name='title',
        ),
    ]
