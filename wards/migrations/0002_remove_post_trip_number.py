# Generated by Django 2.1 on 2020-02-16 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='trip_number',
        ),
    ]
