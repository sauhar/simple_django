# Generated by Django 4.0.6 on 2022-07-21 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2022, 7, 21, 13, 26, 56, 750259))),
            ],
        ),
    ]
