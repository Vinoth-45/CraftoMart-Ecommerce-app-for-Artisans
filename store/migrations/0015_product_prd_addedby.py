# Generated by Django 4.0.3 on 2022-05-31 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_customer_user_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prd_addedBy',
            field=models.CharField(max_length=200, null=True),
        ),
    ]