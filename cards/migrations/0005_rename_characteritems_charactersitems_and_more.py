# Generated by Django 5.1.7 on 2025-04-08 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0004_alter_classtraits_unique_together_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CharacterItems",
            new_name="CharactersItems",
        ),
        migrations.RenameModel(
            old_name="CharacterNotes",
            new_name="CharactersNotes",
        ),
        migrations.RenameModel(
            old_name="CharacterResource",
            new_name="CharactersResource",
        ),
        migrations.RenameModel(
            old_name="CharacterSpell",
            new_name="CharactersSpell",
        ),
        migrations.RenameModel(
            old_name="CharacterTraits",
            new_name="CharactersTraits",
        ),
    ]
