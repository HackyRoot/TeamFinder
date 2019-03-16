# Generated by Django 2.1.7 on 2019-03-16 09:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0006_auto_20190316_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_lead_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2019, 3, 16, 9, 17, 15, 399329, tzinfo=utc)),
        ),
    ]
