# Generated by Django 3.2.4 on 2021-06-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
