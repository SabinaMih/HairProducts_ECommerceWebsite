# Generated by Django 3.1.3 on 2020-12-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='category',
            field=models.ManyToManyField(blank=True, to='shop.Category'),
        ),
    ]
