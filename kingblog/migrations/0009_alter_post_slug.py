# Generated by Django 4.0.3 on 2022-07-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingblog', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]
