# Generated by Django 4.0.3 on 2022-06-24 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badania', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlecenie',
            name='data',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='godzina',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]