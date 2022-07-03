# Generated by Django 4.0.3 on 2022-07-01 21:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kingblog', '0003_alter_comments_created_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 21, 26, 14, 224076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 21, 26, 14, 223539, tzinfo=utc)),
        ),
    ]
