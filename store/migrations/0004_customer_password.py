# Generated by Django 4.0.3 on 2022-05-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_name_customer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
