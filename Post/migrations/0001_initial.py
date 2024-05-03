# Generated by Django 4.1.3 on 2024-05-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(blank=True, max_length=128, null=True)),
                ('Fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('Autor', models.CharField(blank=True, max_length=128, null=True)),
                ('Imagen', models.URLField(blank=True, max_length=1024, null=True)),
                ('Contenido', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
