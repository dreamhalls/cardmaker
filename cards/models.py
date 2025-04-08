from django.db import models

class RuleSystem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=10, default='1.0')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Characters(models.Model):
    name = models.CharField(max_length=255)
    player_name = models.CharField(max_length=255, null=True)
    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Attributes(models.Model):
    TYPE_CHOICES = [
        ('ability', 'Ability'),
        ('skill', 'Skill'),
        ('save', 'Save'),
        ('hp', 'hp'),
    ]

    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)
    default_value = models.CharField(max_length=50, default='0')

    class Meta:
        unique_together = ('key', 'rule_system')

    def __str__(self):
        return self.name

class Classes(models.Model):
    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    hit_die = models.CharField(max_length=10, blank=True, null=True)
    is_official = models.BooleanField(default=True)

    class Meta:
        unique_together = ('key', 'rule_system')

    def __str__(self):
        return self.name

class ClassLevelFeatures(models.Model):
    TYPE_CHOICES = [
        ('attribute', 'Attribute'),
        ('trait', 'Trait'),
        ('skill', 'Skill'),
        ('proficiency', 'Proficiency'),
        ('special', 'Special'),
    ]

    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    level = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    config_json = models.TextField()

    class Meta:
        unique_together = ('classes', 'level', 'type')

    def __str__(self):
        return f'{self.classes.name} - Level {self.level} {self.type}'

class Traits(models.Model):
    STACK_TYPE_CHOICES = [
        ('none', 'None'),
        ('stack', 'Stack'),
        ('best', 'Best'),
        ('unique', 'Unique'),
    ]

    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    key = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    stack_type = models.CharField(max_length=10, choices=STACK_TYPE_CHOICES, blank=True, null=True)
    max_stacks = models.IntegerField(default=1)

    class Meta:
        unique_together = ('key', 'rule_system')

    def __str__(self):
        return self.name

class TraitEffects(models.Model):
    EFFECT_TYPE_CHOICES = [
        ('modifier', 'Modifier'),
        ('replacement', 'Replacement'),
        ('grant', 'Grant'),
        ('condition', 'Condition'),
    ]

    traits = models.ForeignKey(Traits, on_delete=models.CASCADE)
    effect_type = models.CharField(max_length=20, choices=EFFECT_TYPE_CHOICES, blank=True, null=True)
    condition_json = models.TextField(blank=True, null=True)
    modifier_json = models.TextField()
    priority = models.IntegerField(default=50)

    def __str__(self):
        return f'{self.traits.name} - {self.effect_type}'

class Spells(models.Model):
    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    spell_level = models.IntegerField(default=0)
    mp_cost = models.IntegerField(blank=True, null=True)
    save_dc = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    rule_system = models.ForeignKey(RuleSystem, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    rarity = models.IntegerField(default=1)
    icon = models.CharField(max_length=255)


class CharactersAttributes(models.Model):
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        unique_together = ('characters', 'attributes')

    def __str__(self):
        return f'{self.characters.name} - {self.attributes.name}: {self.value}'

class CharactersTraits(models.Model):
    SOURCE_CHOICES = [
        ('class', 'Class'),
        ('race', 'Race'),
        ('item', 'Item'),
        ('feat', 'Feat'),
    ]

    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    traits = models.ForeignKey(Traits, on_delete=models.CASCADE)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    obtained_level = models.IntegerField()

    def __str__(self):
        return f'{self.characters.name} - {self.traits.name}'

class CharactersSpell(models.Model):
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spells, on_delete=models.CASCADE)

class CharactersItems(models.Model):
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)

class CharactersResource(models.Model):
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    long_rest = models.BooleanField(default=False)
    short_rest = models.BooleanField(default=False)
    value = models.IntegerField(default=0)


class CharactersNotes(models.Model):
    TYPE_CHOICES = [
        ('backgrounds', 'Backgrounds'),
        ('notes', 'Notes'),
    ]
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    context = models.CharField(max_length=255)

