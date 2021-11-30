from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cui', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('secondName', models.CharField(max_length=100)),
                ('firstSurname', models.CharField(max_length=100)),
                ('secondSurname', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cui', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('secondName', models.CharField(max_length=100)),
                ('firstSurname', models.CharField(max_length=100)),
                ('secondSurname', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
