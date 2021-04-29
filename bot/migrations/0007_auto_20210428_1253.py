# Generated by Django 3.2 on 2021-04-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_asset_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='limit',
            field=models.FloatField(default=0, verbose_name='граница изменения цены'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='mv',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='asset',
            name='price',
            field=models.FloatField(default=0, verbose_name='цена'),
        ),
    ]
