# Generated by Django 4.1 on 2022-09-04 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insumos_db', to='insumo.marca'),
        ),
    ]
