# Generated by Django 2.2.4 on 2019-09-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0004_auto_20190904_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.CharField(error_messages={'unique': 'This blockID already exists.'}, max_length=264),
        ),
    ]