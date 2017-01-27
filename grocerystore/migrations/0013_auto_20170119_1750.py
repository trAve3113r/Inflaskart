# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0012_auto_20170112_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'ordering': ['parent', 'sub_category_name'], 'verbose_name': 'product sub-category', 'verbose_name_plural': 'product sub-categories'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['store_name', 'store_city', 'store_location']},
        ),
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='top_category',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='sub_category_1',
            new_name='sub_category_name',
        ),
    ]
