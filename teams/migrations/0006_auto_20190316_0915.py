# Generated by Django 2.1.7 on 2019-03-16 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20190316_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 3, 16, 9, 15, 6, 35295, tzinfo=utc)),
        ),
    ]