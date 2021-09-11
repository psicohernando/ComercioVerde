# Generated by Django 3.2.7 on 2021-09-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreAlimento', models.CharField(blank=True, max_length=100, null=True)),
                ('PrecioAlimento', models.FloatField(blank=True, max_length=7, null=True)),
                ('Fotoalimento', models.ImageField(blank=True, null=True, upload_to='')),
                ('FechaelaboracionAl', models.DateField(blank=True, null=True)),
                ('FechavencimientoAl', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
