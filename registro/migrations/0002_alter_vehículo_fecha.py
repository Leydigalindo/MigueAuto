# Generated by Django 4.1 on 2022-09-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehículo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
