# Generated by Django 2.2.19 on 2022-11-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(verbose_name='Номер лаборатории')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Время старта работы')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name='Время конца работы')),
                ('operator', models.IntegerField(verbose_name='Номер оператора')),
                ('task', models.IntegerField(verbose_name='Номер работы')),
            ],
        ),
    ]