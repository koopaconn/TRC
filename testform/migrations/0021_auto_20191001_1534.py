# Generated by Django 2.2.4 on 2019-10-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0020_auto_20191001_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.CharField(error_messages={'unique': 'This Block ID already exists.'}, max_length=264, unique=True),
        ),
    ]
