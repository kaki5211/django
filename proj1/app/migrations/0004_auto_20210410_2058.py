# Generated by Django 3.1.7 on 2021-04-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210402_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='contents',
            field=models.CharField(max_length=1024, null=True, verbose_name='コンテンツ'),
        ),
        migrations.AddField(
            model_name='category',
            name='members',
            field=models.ManyToManyField(related_name='members_ct', to='app.Member'),
        ),
        migrations.AlterField(
            model_name='manage',
            name='contents',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='manage',
            name='youtube_video_id',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
