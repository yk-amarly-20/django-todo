# Generated by Django 2.2.5 on 2020-02-14 09:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todo_dead_line'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='categry',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='todo',
            name='dead_line',
            field=models.DateField(default=datetime.datetime(2020, 2, 14, 9, 53, 26, 648176, tzinfo=utc), verbose_name='締め切り'),
        ),
    ]
