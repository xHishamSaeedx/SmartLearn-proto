# Generated by Django 4.1.4 on 2023-01-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0007_timetable_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='start_date',
        ),
    ]
