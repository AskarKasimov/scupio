# Generated by Django 2.2.19 on 2022-11-24 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_auto_20221124_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='field',
        ),
    ]
