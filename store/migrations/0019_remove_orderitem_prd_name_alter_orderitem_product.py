# Generated by Django 4.0.3 on 2022-06-12 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_orderitem_prd_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='prd_name',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
