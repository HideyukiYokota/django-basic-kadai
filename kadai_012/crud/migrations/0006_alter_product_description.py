# Generated by Django 4.2.4 on 2023-08-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
