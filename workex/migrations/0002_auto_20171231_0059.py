# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateField(verbose_name='FromDate'),
        ),
        migrations.RemoveField(
            model_name='experience',
            name='listed_description',
        ),
        migrations.AddField(
            model_name='experience',
            name='listed_description',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='workex.ExperienceDesc'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(verbose_name='ToDate'),
        ),
    ]
