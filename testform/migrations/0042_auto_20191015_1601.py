# Generated by Django 2.2.4 on 2019-10-15 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0041_auto_20191015_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
