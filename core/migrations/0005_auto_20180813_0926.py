# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180813_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='current_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='core.Location'),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='nearest_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nearest_city', to='core.Location'),
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='preferred_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_location', to='core.Location'),
        ),
    ]
