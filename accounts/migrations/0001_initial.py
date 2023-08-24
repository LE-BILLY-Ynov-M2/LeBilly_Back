# Generated by Django 4.1.2 on 2022-11-23 10:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('username', models.CharField(blank=True, max_length=45)),
                ('profession', models.CharField(blank=True, max_length=45)),
                ('telephone', models.CharField(blank=True, max_length=45, null=True)),
                ('profile', models.CharField(blank=True, choices=[('createur', 'createur')], max_length=255, null=True)),
                ('genre', models.CharField(blank=True, choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Other', 'Other'), ('None', 'None')], max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('code', models.CharField(blank=True, max_length=5, null=True)),
                ('bithrDay', models.DateField(default=datetime.date.today)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
