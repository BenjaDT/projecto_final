# Generated by Django 5.0.6 on 2024-05-24 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contacto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField(max_length=8)),
                ('fecha_de_precio', models.DateField(null=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('provedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.provedor')),
            ],
        ),
    ]
