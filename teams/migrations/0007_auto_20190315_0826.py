# Generated by Django 2.1.7 on 2019-03-15 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20190315_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(default='hacky', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
