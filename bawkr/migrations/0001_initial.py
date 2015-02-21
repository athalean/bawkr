# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bawk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-posted_on'],
            },
            bases=(models.Model,),
        ),
    ]
