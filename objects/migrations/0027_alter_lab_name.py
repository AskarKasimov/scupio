# Generated by Django 4.1.3 on 2023-04-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0026_alter_object_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='name',
            field=models.IntegerField(unique=True, verbose_name='Номер лаборатории'),
        ),
    ]