# Generated by Django 2.1.15 on 2021-11-09 03:02

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cad_mapeamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cad_itens_auditaveis',
            name='fr',
            field=models.IntegerField(),
        ),
    ]
