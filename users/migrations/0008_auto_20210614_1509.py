# Generated by Django 3.2.4 on 2021-06-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210614_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_role',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
