# Generated by Django 2.2.4 on 2019-10-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0038_auto_20191009_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthDec',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='LeftLWidthInc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='centerLWidthInc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthDec',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='gutterWidthInc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthDec',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='rightLWidthInc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthDec',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='shoulderWidthInc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
