# Generated by Django 3.0.8 on 2020-12-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
    ]
