# Generated by Django 4.0.6 on 2023-02-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_property_propertytag_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]
