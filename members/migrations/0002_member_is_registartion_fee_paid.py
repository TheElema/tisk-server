# Generated by Django 2.0.3 on 2018-05-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_registartion_fee_paid',
            field=models.BooleanField(default=False),
        ),
    ]
