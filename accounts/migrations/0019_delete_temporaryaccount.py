# Generated by Django 3.2.19 on 2023-08-23 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_temporaryaccount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TemporaryAccount',
        ),
    ]
