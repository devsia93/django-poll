# Generated by Django 2.2.10 on 2021-09-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='type',
            field=models.IntegerField(choices=[(0, 'RadioButton'), (1, 'CheckBox'), (2, 'TextBox')], default=0, verbose_name='Тип'),
        ),
    ]
