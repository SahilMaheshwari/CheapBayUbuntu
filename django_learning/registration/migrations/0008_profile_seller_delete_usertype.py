# Generated by Django 5.0.6 on 2024-06-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_usertype_is_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
