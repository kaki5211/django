# Generated by Django 3.1.7 on 2021-04-17 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210417_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='category_id',
            field=models.ForeignKey(blank=True, db_column='category_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
