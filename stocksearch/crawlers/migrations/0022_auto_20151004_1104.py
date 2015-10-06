# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawlers', '0021_auto_20151003_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawler',
            name='origin',
            field=models.CharField(max_length=2, choices=[('PX', 'Pexels'), ('MG', 'Magdeleine'), ('FC', 'FancyCrave'), ('SS', 'StockSnap'), ('PB', 'PixaBay'), ('TP', 'tookapic'), ('KP', 'kaboompics'), ('PJ', 'picjumbo'), ('LS', 'LibreShot'), ('LV', 'Littlevisuals')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='origin',
            field=models.CharField(max_length=2, choices=[('PX', 'Pexels'), ('MG', 'Magdeleine'), ('FC', 'FancyCrave'), ('SS', 'StockSnap'), ('PB', 'PixaBay'), ('TP', 'tookapic'), ('KP', 'kaboompics'), ('PJ', 'picjumbo'), ('LS', 'LibreShot'), ('LV', 'Littlevisuals')]),
        ),
    ]
