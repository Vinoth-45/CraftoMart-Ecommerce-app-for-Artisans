# Generated by Django 4.0.3 on 2022-06-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_orderitem_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
