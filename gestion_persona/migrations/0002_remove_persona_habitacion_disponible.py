# Generated by Django 4.2 on 2023-05-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_persona', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='habitacion_disponible',
        ),
    ]
