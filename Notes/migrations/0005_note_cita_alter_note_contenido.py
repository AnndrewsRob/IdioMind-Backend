# Generated by Django 4.1.3 on 2024-04-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0004_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='cita',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AlterField(
            model_name='note',
            name='contenido',
            field=models.CharField(default='', max_length=511),
        ),
    ]
