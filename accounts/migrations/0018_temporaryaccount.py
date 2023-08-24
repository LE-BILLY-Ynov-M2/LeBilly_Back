# Generated by Django 3.2.19 on 2023-08-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_account_activation_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('activation_code', models.CharField(max_length=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
