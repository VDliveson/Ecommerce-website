# Generated by Django 3.2.8 on 2021-10-26 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 26, 18, 11, 11, 575330)),
        ),
    ]