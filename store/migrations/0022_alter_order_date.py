# Generated by Django 3.2.8 on 2021-10-25 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 26, 0, 43, 57, 393976)),
        ),
    ]
