# Generated by Django 4.2.7 on 2023-12-05 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_company_service_photo_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_photo',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ser_ph_set', to='services.service'),
        ),
    ]