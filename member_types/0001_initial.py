# Generated by Django 2.0.3 on 2018-05-23 09:47

import colorfield.fields
from django.db import migrations, models
import tisk.utils


def insert_defaults(apps, schema_editor):
    MemberType = apps.get_model("member_types", "MemberType")
    MemberType(name="Investor Business", package="Terabyte").save()
    MemberType(name="Investor Individual", package="Terabyte").save()
    MemberType(name="Business", package="Gigabyte").save()
    MemberType(name="Professional", package="Megabyte").save()
    MemberType(name="Student", package="Kilobyte").save()
    MemberType(name="Futures", package="Microbyte", active=False).save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('monthly_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('package', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('registration_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('share_capital', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=tisk.utils.get_image_path)),
                ('color', colorfield.fields.ColorField(blank=True, max_length=18, null=True)),
            ],
        ),
        migrations.RunPython(insert_defaults)
    ]
