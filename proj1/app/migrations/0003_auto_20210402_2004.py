# Generated by Django 3.1.6 on 2021-04-02 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210402_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', default='1', on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
