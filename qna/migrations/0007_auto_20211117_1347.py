# Generated by Django 3.2.9 on 2021-11-17 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0006_auto_20211117_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 5, 47, 52, 621213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 5, 47, 52, 226766, tzinfo=utc)),
        ),
    ]
