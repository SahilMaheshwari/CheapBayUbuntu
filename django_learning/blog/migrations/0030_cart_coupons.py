# Generated by Django 5.0.6 on 2024-06-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_alter_discountcodes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='blog.discountcodes'),
        ),
    ]
