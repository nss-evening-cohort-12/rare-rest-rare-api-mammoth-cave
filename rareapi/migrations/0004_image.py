# Generated by Django 3.1.4 on 2021-01-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_file', models.FileField(upload_to='pics/')),
            ],
        ),
    ]
