# Generated by Django 4.0.6 on 2022-07-22 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_name_video_title_alter_video_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='charge',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 18, 50, 7, 528900)),
        ),
    ]