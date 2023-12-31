# Generated by Django 4.1.2 on 2023-01-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='profession',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='profil',
            name='adress',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='lastname',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='profil',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
