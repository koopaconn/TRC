# Generated by Django 2.1.1 on 2018-11-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_testform',
            name='email',
            field=models.CharField(default='N/A', max_length=264),
            preserve_default=False,
        ),
    ]
