# Generated by Django 3.2.19 on 2023-08-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_account_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]