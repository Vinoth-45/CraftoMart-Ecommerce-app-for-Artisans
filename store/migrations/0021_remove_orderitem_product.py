# Generated by Django 4.0.3 on 2022-06-12 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]
