# Generated by Django 3.1.4 on 2021-01-07 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_auto_20201219_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', related_query_name='author', to='rareapi.rareuser')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', related_query_name='follower', to='rareapi.rareuser')),
            ],
        ),
    ]