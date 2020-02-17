# Generated by Django 2.2.4 on 2019-10-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0022_auto_20191002_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthDec',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthInc',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.BigIntegerField(error_messages={'unique': 'This Block ID already exists.'}, unique=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='centerLWidthDec',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='centerLWidthInc',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthDec',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthInc',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthDec',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthInc',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthDec',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthInc',
            field=models.BigIntegerField(),
        ),
    ]
