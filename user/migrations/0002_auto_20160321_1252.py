# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentparent',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='studentparent',
            old_name='student_id',
            new_name='student',
        ),
    ]
