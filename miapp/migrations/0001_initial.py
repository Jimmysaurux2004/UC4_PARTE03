# Generated by Django 4.2.13 on 2024-07-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apepat', models.CharField(max_length=50)),
                ('apemat', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]