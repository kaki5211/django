# Generated by Django 3.2 on 2021-05-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_category_contents_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('action', 'アクション'), ('adventure', 'アドベンチャー'), ('youth', '青春'), ('love', '恋愛'), ('sf', 'SF'), ('history', '時代'), ('mystery', 'ミステリー'), ('comedy', 'コメディー'), ('horror', 'ホラー')], max_length=20, verbose_name='カテゴリー'),
        ),
    ]
