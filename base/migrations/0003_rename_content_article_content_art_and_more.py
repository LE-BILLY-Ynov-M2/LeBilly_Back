# Generated by Django 4.1.2 on 2023-04-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_article_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='content_art',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created_date',
            new_name='created_date_art',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='title_art',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='user_art',
        ),
    ]
