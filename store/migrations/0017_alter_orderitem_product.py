# Generated by Django 4.0.3 on 2022-06-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_orderitem_prd_addedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
