# Generated by Django 3.2 on 2021-04-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('product', models.CharField(max_length=20)),
                ('limit', models.DecimalField(decimal_places=8, default=0, max_digits=20, verbose_name='граница изменения цены')),
                ('volume', models.IntegerField(default=0, verbose_name='количество')),
                ('price', models.DecimalField(decimal_places=8, default=0, max_digits=20, verbose_name='цена')),
                ('status', models.CharField(choices=[('OPEN', 'open'), ('CLOSE', 'close')], max_length=10)),
            ],
            options={
                'verbose_name': 'Актив',
                'verbose_name_plural': 'Активы',
            },
        ),
    ]