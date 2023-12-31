# Generated by Django 3.2.19 on 2023-08-23 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='activation_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
