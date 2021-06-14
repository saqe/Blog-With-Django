# Generated by Django 3.2 on 2021-06-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210610_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='zip code'),
        ),
    ]
