# Generated by Django 4.0.3 on 2022-06-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='prd_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]