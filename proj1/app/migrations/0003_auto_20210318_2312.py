# Generated by Django 3.1.6 on 2021-03-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210316_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='manage_twitter_already',
            field=models.BooleanField(default=False),
        ),
    ]