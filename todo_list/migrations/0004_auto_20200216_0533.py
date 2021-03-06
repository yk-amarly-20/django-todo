# Generated by Django 2.2.5 on 2020-02-16 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20200214_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='dead_line',
            field=models.DateField(default=datetime.datetime(2020, 2, 16, 5, 33, 36, 693655, tzinfo=utc), verbose_name='締め切り'),
        ),
    ]
