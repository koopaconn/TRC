# Generated by Django 2.2.4 on 2019-10-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0013_auto_20191001_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_testform',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.CharField(error_messages={'unique': 'This Block ID already exists.'}, max_length=264, unique=True),
        ),
    ]
