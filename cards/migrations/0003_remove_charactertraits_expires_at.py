# Generated by Django 5.1.7 on 2025-03-31 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_characters_player_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="charactertraits",
            name="expires_at",
        ),
    ]
