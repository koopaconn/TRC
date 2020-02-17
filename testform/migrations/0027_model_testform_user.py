# Generated by Django 2.2.4 on 2019-10-09 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testform', '0026_auto_20191009_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_testform',
            name='user',
            field=models.ForeignKey(default='oldval', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
