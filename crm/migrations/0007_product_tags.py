# Generated by Django 3.0.8 on 2020-12-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_order_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='crm.Tags'),
        ),
    ]