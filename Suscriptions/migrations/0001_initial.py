# Generated by Django 4.1.3 on 2024-05-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_suscription', models.CharField(max_length=45)),
                ('estado', models.BooleanField(default=True)),
                ('dias_duracion', models.IntegerField()),
            ],
        ),
    ]
