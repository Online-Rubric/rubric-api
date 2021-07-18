# Generated by Django 3.2.5 on 2021-07-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubrics', '0003_rubric_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubric',
            old_name='score',
            new_name='Asked meaningful clarifying questions',
        ),
        migrations.AddField(
            model_name='rubric',
            name='Identified inputs and outputs \t\t',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rubric',
            name='Identified optimal data structure and/or algorithm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rubric',
            name='Visually illustrated the problem domain',
            field=models.IntegerField(default=0),
        ),
    ]
