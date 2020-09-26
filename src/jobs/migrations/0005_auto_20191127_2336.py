# Generated by Django 2.2.6 on 2019-11-27 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobpost_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 4, 19, 6, 32, 84928, tzinfo=utc), verbose_name='Job Expiration Date'),
        ),
    ]
