# Generated by Django 2.1.7 on 2019-03-16 16:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20190316_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 3, 16, 16, 29, 37, 929389, tzinfo=utc)),
        ),
    ]