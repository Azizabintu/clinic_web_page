# Generated by Django 4.2.7 on 2023-12-01 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_photo',
            old_name='company',
            new_name='service',
        ),
    ]