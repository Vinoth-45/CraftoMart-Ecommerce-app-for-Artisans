# Generated by Django 4.0.3 on 2022-05-29 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
