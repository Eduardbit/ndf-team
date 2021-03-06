# Generated by Django 2.0.4 on 2018-04-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180404_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='birthday',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='players',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='players',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='players',
            name='number',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=0, max_digits=3, null=True, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='players',
            name='vk_id',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Страница VK'),
        ),
        migrations.AlterField(
            model_name='players',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='Вес'),
        ),
    ]
