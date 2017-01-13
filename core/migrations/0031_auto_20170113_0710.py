# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_email_flags'),
    ]

    database_operations = [
        migrations.AlterModelTable('Story', 'story_story')
    ]

    state_operations = [
        migrations.DeleteModel('Story')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
