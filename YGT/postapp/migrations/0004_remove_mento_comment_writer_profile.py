# Generated by Django 4.0.6 on 2022-07-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_mento_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mento_comment',
            name='writer_profile',
        ),
    ]
