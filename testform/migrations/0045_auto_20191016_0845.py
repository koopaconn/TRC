# Generated by Django 2.2.4 on 2019-10-16 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testform', '0044_auto_20191016_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_testform',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='model_testform',
            name='editBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
