# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-03 10:33
from __future__ import unicode_literals

from django.db import migrations


def create_submission_configuration(apps, schema_editor):
    Journal = apps.get_model('journal', 'Journal')
    Configuration = apps.get_model('submission', 'SubmissionConfiguration')

    journals = Journal.objects.all()

    for journal in journals:
        new_configuration = Configuration.objects.create(journal=journal)


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0022_submissionconfiguration'),
    ]

    operations = [
        migrations.RunPython(create_submission_configuration)
    ]
