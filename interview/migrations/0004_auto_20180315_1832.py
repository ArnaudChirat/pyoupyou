# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-15 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("interview", "0003_auto_20171114_2233")]

    operations = [
        migrations.RenameField(model_name="process", old_name="closed_reason", new_name="state"),
        migrations.AlterField(
            model_name="interview",
            name="next_state",
            field=models.CharField(
                choices=[
                    ("NP", "NEED PLANIFICATION"),
                    ("PL", "PLANNED"),
                    ("GO", "GO"),
                    ("NO", "NO"),
                    ("DR", "DRAFT"),
                    ("WI", "WAIT INFORMATION"),
                ],
                max_length=3,
                verbose_name="next state",
            ),
        ),
    ]
