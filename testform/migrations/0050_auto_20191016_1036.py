# Generated by Django 2.2.4 on 2019-10-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0049_model_testform_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='username',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
    ]
