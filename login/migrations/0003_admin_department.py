# Generated by Django 2.0.4 on 2018-05-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180504_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='department',
            field=models.IntegerField(default=1),
        ),
    ]
