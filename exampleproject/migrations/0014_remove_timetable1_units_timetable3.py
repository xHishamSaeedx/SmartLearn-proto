# Generated by Django 4.1.4 on 2023-01-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0013_timetable2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable1',
            name='units',
        ),
        migrations.CreateModel(
            name='Timetable3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.ManyToManyField(blank=True, to='exampleproject.unit')),
            ],
        ),
    ]
