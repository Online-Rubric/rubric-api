# Generated by Django 3.2.5 on 2021-07-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0009_auto_20210721_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='communicate_effectively_notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]