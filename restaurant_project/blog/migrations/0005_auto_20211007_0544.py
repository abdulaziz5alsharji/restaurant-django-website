# Generated by Django 3.2.4 on 2021-10-07 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211001_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 5, 44, 52, 794741)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 5, 44, 52, 793742)),
        ),
    ]
