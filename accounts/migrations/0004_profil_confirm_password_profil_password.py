# Generated by Django 4.1.2 on 2023-02-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='profil',
            name='password',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
