# Generated by Django 4.1.4 on 2023-01-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0024_remove_timetable1_subjects_whatsubjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjecthrs',
            name='priority',
            field=models.CharField(default='0', max_length=400),
        ),
    ]