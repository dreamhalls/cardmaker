from rest_framework import serializers
from .models import RuleSystem, Characters, Attributes, Classes, Traits, ClassLevelFeatures, CharactersTraits

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = '__all__'

class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class TraitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traits
        fields = '__all__'

class ClassLevelFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevelFeatures
        fields = '__all__'

class CharacterTraitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharactersTraits
        fields = '__all__'

class RuleSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleSystem
        fields = '__all__'

