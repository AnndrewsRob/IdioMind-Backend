# Generated by Django 4.1.3 on 2024-04-21 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_rename_fecha_creacion_note_fecha_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='idDocumento',
            new_name='documento',
        ),
    ]