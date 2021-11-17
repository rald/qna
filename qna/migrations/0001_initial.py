# Generated by Django 3.2.9 on 2021-11-17 05:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 11, 17, 5, 21, 58, 363059, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 11, 17, 5, 21, 58, 834029, tzinfo=utc))),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_answer', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.question')),
            ],
        ),
    ]