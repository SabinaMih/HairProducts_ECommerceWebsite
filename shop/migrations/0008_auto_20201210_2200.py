# Generated by Django 3.1.3 on 2020-12-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201210_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='category',
            field=models.ManyToManyField(blank=True, to='shop.Category'),
        ),
    ]
