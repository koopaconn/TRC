# Generated by Django 2.2.4 on 2019-10-01 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0012_auto_20191001_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='blockID',
            field=models.OneToOneField(error_messages={'unique': 'This Block ID already exists.'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
