# Generated by Django 3.0.8 on 2020-12-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
