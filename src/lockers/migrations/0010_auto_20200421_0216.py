# Generated by Django 3.0.5 on 2020-04-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0009_auto_20200421_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupancy',
            name='id',
        ),
        migrations.AlterField(
            model_name='occupancy',
            name='lockerid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]