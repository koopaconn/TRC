# Generated by Django 2.2.4 on 2019-10-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0023_auto_20191002_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthDec',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthInc',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.CharField(error_messages={'unique': 'This Block ID already exists.'}, max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='centerLWidthDec',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='centerLWidthInc',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthDec',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthInc',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthDec',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthInc',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthDec',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthInc',
            field=models.CharField(max_length=264),
        ),
    ]
