# Generated by Django 3.2 on 2021-06-10 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210602_0642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-posted_datetime']},
        ),
    ]
