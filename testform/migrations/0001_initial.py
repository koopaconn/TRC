# Generated by Django 2.1.1 on 2018-11-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_testform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('agency', models.CharField(max_length=264)),
                ('juristiction', models.CharField(max_length=264)),
                ('postitle', models.CharField(max_length=264)),
                ('page', models.CharField(max_length=264)),
                ('comment', models.CharField(max_length=264)),
            ],
        ),
    ]
