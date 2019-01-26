# Generated by Django 1.10.8 on 2017-10-03 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0003_privatepost_hat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privateposts', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
    ]
