# Generated by Django 3.1.4 on 2020-12-19 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_id',
            new_name='user_id',
        ),
    ]
