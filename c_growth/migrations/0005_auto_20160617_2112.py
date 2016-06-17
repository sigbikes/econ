# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_growth', '0004_auto_20160617_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='compoundings',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='data',
            name='interest',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='principle',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='rate',
            field=models.DecimalField(decimal_places=3, default=0.05, max_digits=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='year',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Compounding',
        ),
        migrations.DeleteModel(
            name='Gains',
        ),
        migrations.DeleteModel(
            name='Principle',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.DeleteModel(
            name='Sum',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]