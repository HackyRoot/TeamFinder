# Generated by Django 2.1.7 on 2019-03-20 15:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_auto_20190320_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 3, 20, 15, 59, 11, 215751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_lead',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_lead_key', to=settings.AUTH_USER_MODEL),
        ),
    ]