# Generated by Django 3.2.8 on 2021-10-25 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 25, 20, 2, 16, 813641)),
        ),
    ]
