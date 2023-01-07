# Generated by Django 4.1.4 on 2023-01-04 14:09

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0005_timetable_remove_classproject_demo_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timetable',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='exampleproject.subject'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='units',
            field=models.ManyToManyField(blank=True, to='exampleproject.unit'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='weekday_hrs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='weekend_hrs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
