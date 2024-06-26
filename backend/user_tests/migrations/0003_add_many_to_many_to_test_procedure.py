# Generated by Django 5.0.4 on 2024-05-15 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tests', '0002_add_user_list_to_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testprocedure',
            name='acceptance_test',
        ),
        migrations.AddField(
            model_name='testprocedure',
            name='acceptance_tests',
            field=models.ManyToManyField(blank=True, null=True, to='user_tests.useracceptancetest'),
        ),
        migrations.AddField(
            model_name='testprocedure',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_tests.project', verbose_name='Projekt'),
        ),
    ]
