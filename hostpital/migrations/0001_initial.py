# Generated by Django 3.2.9 on 2021-11-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historyNumber', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('secondName', models.CharField(max_length=100)),
                ('firtSurname', models.CharField(max_length=100)),
                ('secondSurname', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
    ]
