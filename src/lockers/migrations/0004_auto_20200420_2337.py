# Generated by Django 3.0.5 on 2020-04-20 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0003_auto_20200420_2227'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='occupancy',
            unique_together={('lockerid', 'date')},
        ),
    ]
