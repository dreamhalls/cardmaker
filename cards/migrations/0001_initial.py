# Generated by Django 5.1.7 on 2025-03-30 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=255)),
                ("hit_die", models.CharField(blank=True, max_length=10, null=True)),
                ("is_official", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="RuleSystem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("version", models.CharField(default="1.0", max_length=10)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ClassLevelFeatures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("attribute", "Attribute"),
                            ("trait", "Trait"),
                            ("skill", "Skill"),
                            ("proficiency", "Proficiency"),
                            ("special", "Special"),
                        ],
                        max_length=20,
                    ),
                ),
                ("config_json", models.TextField()),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.classes"
                    ),
                ),
            ],
            options={
                "unique_together": {("classes", "level", "type")},
            },
        ),
        migrations.AddField(
            model_name="classes",
            name="rule_system",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cards.rulesystem"
            ),
        ),
        migrations.CreateModel(
            name="Characters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "rule_system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.rulesystem",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attributes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ability", "Ability"),
                            ("skill", "Skill"),
                            ("save", "Save"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("default_value", models.CharField(default="0", max_length=50)),
                (
                    "rule_system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.rulesystem",
                    ),
                ),
            ],
            options={
                "unique_together": {("key", "rule_system")},
            },
        ),
        migrations.CreateModel(
            name="Traits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=255)),
                (
                    "stack_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("none", "None"),
                            ("stack", "Stack"),
                            ("best", "Best"),
                            ("unique", "Unique"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("max_stacks", models.IntegerField(default=1)),
                (
                    "rule_system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.rulesystem",
                    ),
                ),
            ],
            options={
                "unique_together": {("key", "rule_system")},
            },
        ),
        migrations.CreateModel(
            name="TraitEffects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "effect_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("modifier", "Modifier"),
                            ("replacement", "Replacement"),
                            ("grant", "Grant"),
                            ("condition", "Condition"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("condition_json", models.TextField(blank=True, null=True)),
                ("modifier_json", models.TextField()),
                ("priority", models.IntegerField(default=50)),
                (
                    "traits",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.traits"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CharacterTraits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("class", "Class"),
                            ("race", "Race"),
                            ("item", "Item"),
                            ("feat", "Feat"),
                        ],
                        max_length=10,
                    ),
                ),
                ("obtained_level", models.IntegerField()),
                ("expires_at", models.DateTimeField(blank=True, null=True)),
                (
                    "characters",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.characters",
                    ),
                ),
                (
                    "traits",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.traits"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassSkills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("min_level", models.IntegerField(default=1)),
                (
                    "attributes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.attributes",
                    ),
                ),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.classes"
                    ),
                ),
            ],
            options={
                "unique_together": {("classes", "attributes")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="classes",
            unique_together={("key", "rule_system")},
        ),
        migrations.CreateModel(
            name="ClassTraits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unlock_level", models.IntegerField(default=1)),
                (
                    "class_level_features",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.classlevelfeatures",
                    ),
                ),
                (
                    "traits",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.traits"
                    ),
                ),
            ],
            options={
                "unique_together": {("class_level_features", "traits")},
            },
        ),
    ]
