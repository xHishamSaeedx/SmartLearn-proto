# Generated by Django 4.1.4 on 2023-01-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0004_rename_vote_total_topic_rating_alter_unit_weightage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='source_link',
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='classproject',
            name='vote_total',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='tag',
        ),
    ]