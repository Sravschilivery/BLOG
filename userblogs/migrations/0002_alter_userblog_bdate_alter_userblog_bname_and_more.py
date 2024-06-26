# Generated by Django 4.2.6 on 2023-10-31 19:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userblogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='bdate',
            field=models.DateField(default=datetime.datetime(2023, 11, 1, 0, 55, 24, 126342), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='bname',
            field=models.CharField(max_length=100, verbose_name='bloger name'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='buid',
            field=models.ForeignKey(db_column='buid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='bloger id'),
        ),
    ]
