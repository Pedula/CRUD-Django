# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('fk', models.ForeignKey(to='contato.Contato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
