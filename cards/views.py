from django.shortcuts import render
from rest_framework import generics
from .serializers import AttributesSerializer, ClassesSerializer, TraitsSerializer, ClassLevelFeaturesSerializer,CharactersSerializer, CharacterTraitsSerializer, RuleSystemSerializer
from .models import RuleSystem, Characters, Attributes, Classes, Traits, ClassLevelFeatures, CharacterTraits


class RuleSystemListCreate(generics.ListCreateAPIView):
    queryset = RuleSystem.objects.all()
    serializer_class = RuleSystemSerializer

class RuleSystemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RuleSystem.objects.all()
    serializer_class = RuleSystemSerializer

class AttributesListCreate(generics.ListCreateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

class AttributesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

class ClassesListCreate(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class ClassesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class TraitsListCreate(generics.ListCreateAPIView):
    queryset = Traits.objects.all()
    serializer_class = TraitsSerializer

class TraitsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Traits.objects.all()
    serializer_class = TraitsSerializer

class ClassLevelFeaturesListCreate(generics.ListCreateAPIView):
    queryset = ClassLevelFeatures.objects.all()
    serializer_class = ClassLevelFeaturesSerializer

class ClassLevelFeaturesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassLevelFeatures.objects.all()
    serializer_class = ClassLevelFeaturesSerializer

class CharacterTraitsListCreate(generics.ListCreateAPIView):
    queryset = CharacterTraits.objects.all()
    serializer_class = CharacterTraitsSerializer

class CharacterTraitsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CharacterTraits.objects.all()
    serializer_class = CharacterTraitsSerializer

class CharactersListCreate(generics.ListCreateAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer

class CharactersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = CharactersSerializer

