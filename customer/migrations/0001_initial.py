# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-10 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(default=1)),
                ('password', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('profile', models.ImageField(upload_to='~/cokassis/Client/image')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=30)),
                ('search_count', models.IntegerField()),
                ('dish_type', models.BooleanField(default=True)),
                ('mat_type', models.BooleanField(default=True)),
                ('customers', models.ManyToManyField(to='customer.Customer')),
            ],
            options={
                'ordering': ['-keyword', '-search_count'],
            },
        ),
        migrations.CreateModel(
            name='MatQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
