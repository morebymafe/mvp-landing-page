# Generated by Django 3.1.5 on 2021-03-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20210309_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='emailentry',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
