# Generated by Django 2.2.5 on 2020-02-17 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20200216_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dead_line',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 3, 47, 15, 964369, tzinfo=utc), verbose_name='締め切り'),
        ),
    ]
