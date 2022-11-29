# Generated by Django 2.2.19 on 2022-11-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0016_auto_20221124_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='object',
            old_name='date_of_selection',
            new_name='date_selection',
        ),
        migrations.RemoveField(
            model_name='task',
            name='result',
        ),
        migrations.AddField(
            model_name='object',
            name='rock_name',
            field=models.CharField(default='test', max_length=200, verbose_name='Название породы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='result_helium',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат по гелию'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_kerosene',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат по керосин'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_kpr',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат Кпр'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_plm',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат Плм'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_plo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат Пло'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_porosity',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Параметр пористости'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_ues',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат У.Э.С'),
        ),
        migrations.AddField(
            model_name='task',
            name='result_water',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Результат по вода'),
        ),
    ]