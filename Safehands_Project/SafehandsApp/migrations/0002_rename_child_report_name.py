# Generated by Django 4.0 on 2021-12-21 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SafehandsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='child',
            new_name='name',
        ),
    ]
