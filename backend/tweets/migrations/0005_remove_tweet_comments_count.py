# Generated by Django 5.1.2 on 2024-11-09 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0004_like_share"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweet",
            name="comments_count",
        ),
    ]
