# Generated by Django 3.1.6 on 2021-03-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210318_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='youtube_video_day',
            field=models.DateTimeField(null=True),
        ),
    ]