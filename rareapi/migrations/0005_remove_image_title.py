# Generated by Django 3.1.4 on 2021-01-12 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0004_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]