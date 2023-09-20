# Generated by Django 4.1.2 on 2023-09-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0028_alter_evenement_url_youtube"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evenement",
            name="attendees",
        ),
        migrations.AddField(
            model_name="account",
            name="events_user",
            field=models.ManyToManyField(
                blank=True, related_name="attendees", to="accounts.evenement"
            ),
        ),
    ]
