# Generated by Django 3.1.3 on 2020-12-14 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201215_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='event_type',
        ),
    ]