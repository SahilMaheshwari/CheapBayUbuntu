# Generated by Django 5.0.6 on 2024-06-17 02:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_post_discount_discountcodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='coupon_discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
