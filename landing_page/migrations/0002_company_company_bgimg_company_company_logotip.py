# Generated by Django 4.2.7 on 2023-11-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_bgimg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='company_logotip',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
