# Generated by Django 3.0.5 on 2020-04-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0008_auto_20200421_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupancy',
            name='lockerid',
            field=models.IntegerField(),
        ),
    ]
