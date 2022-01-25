# Generated by Django 4.0.1 on 2022-01-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
