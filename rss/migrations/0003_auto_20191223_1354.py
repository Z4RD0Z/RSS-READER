# Generated by Django 3.0 on 2019-12-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0002_auto_20191223_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rss',
            name='link',
            field=models.URLField(max_length=256, verbose_name='link'),
        ),
    ]