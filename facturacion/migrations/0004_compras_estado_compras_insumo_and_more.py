# Generated by Django 4.1 on 2022-09-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0002_alter_insumo_marca'),
        ('facturacion', '0003_compras'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Completa', 'Completa')], default='Activo', max_length=10, verbose_name='Estado de factura'),
        ),
        migrations.AddField(
            model_name='compras',
            name='insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insumo.insumo', verbose_name='inumo'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='tipodeservicio',
            field=models.CharField(choices=[('Latoneria', 'Latoneria'), ('Pintura', 'Pintura')], max_length=10, verbose_name='Seleccione el tipo de servicio'),
        ),
    ]
