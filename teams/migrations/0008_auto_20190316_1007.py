# Generated by Django 2.1.7 on 2019-03-16 10:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20190316_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 3, 16, 10, 7, 9, 208017, tzinfo=utc)),
        ),
    ]