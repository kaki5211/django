# Generated by Django 3.1.7 on 2021-04-22 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210422_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents_demo',
            name='category_key',
            field=models.OneToOneField(blank=True, db_column='category_eng', default=None, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]