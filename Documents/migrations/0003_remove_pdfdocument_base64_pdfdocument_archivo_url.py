# Generated by Django 4.1.3 on 2024-04-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_alter_pdfdocument_fecha_subida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfdocument',
            name='base64',
        ),
        migrations.AddField(
            model_name='pdfdocument',
            name='archivo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
