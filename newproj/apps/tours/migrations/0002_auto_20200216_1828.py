# Generated by Django 2.1.7 on 2020-02-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.RemoveField(
            model_name='tour',
            name='cover',
        ),
        migrations.AlterField(
            model_name='tour',
            name='subtitle',
            field=models.TextField(verbose_name='Подзаголовок'),
        ),
    ]