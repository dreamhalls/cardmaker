from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response  # 导入 Response 类
from .serializers import AttributesSerializer, ClassesSerializer, TraitsSerializer, ClassLevelFeaturesSerializer, CharactersSerializer, CharacterTraitsSerializer, RuleSystemSerializer
from .models import RuleSystem, Characters, Attributes, Classes, Traits, ClassLevelFeatures, CharacterTraits
from cardmaker.utils import CommonResponse
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="列出所有规则系统并创建新的规则系统",
    responses={200: RuleSystemSerializer(many=True)}
)
class RuleSystemListCreate(generics.ListCreateAPIView):
    """
    规则系统列表创建视图，用于获取所有规则系统列表或创建新的规则系统。
    """
    queryset = RuleSystem.objects.all()
    serializer_class = RuleSystemSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有规则系统列表。
        """
        response = super().list(request, *args, **kwargs)
        # 将 CommonResponse 返回的字典包装成 Response 对象
        return Response(CommonResponse.success(data=response.data))

    def create(self, request, *args, **kwargs):
        """
        创建新的规则系统。
        """
        response = super().create(request, *args, **kwargs)
        return Response(CommonResponse.success(data=response.data))


@extend_schema(
    description="获取、更新或删除单个规则系统",
    responses={200: RuleSystemSerializer()}
)
class RuleSystemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    规则系统获取、更新、删除视图，用于获取、更新或删除单个规则系统。
    """
    queryset = RuleSystem.objects.all()
    serializer_class = RuleSystemSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个规则系统。
        """
        response = super().retrieve(request, *args, **kwargs)
        return Response(CommonResponse.success(data=response.data))

    def update(self, request, *args, **kwargs):
        """
        更新单个规则系统。
        """
        response = super().update(request, *args, **kwargs)
        return Response(CommonResponse.success(data=response.data))

    def destroy(self, request, *args, **kwargs):
        """
        删除单个规则系统。
        """
        response = super().destroy(request, *args, **kwargs)
        return Response(CommonResponse.success(data=response.data))


@extend_schema(
    description="列出所有属性并创建新的属性",
    responses={200: AttributesSerializer(many=True)}
)
class AttributesListCreate(generics.ListCreateAPIView):
    """
    属性列表创建视图，用于获取所有属性列表或创建新的属性。
    """
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有属性列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的属性。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个属性",
    responses={200: AttributesSerializer()}
)
class AttributesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    属性获取、更新、删除视图，用于获取、更新或删除单个属性。
    """
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个属性。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个属性。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个属性。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="列出所有职业并创建新的职业",
    responses={200: ClassesSerializer(many=True)}
)
class ClassesListCreate(generics.ListCreateAPIView):
    """
    职业列表创建视图，用于获取所有职业列表或创建新的职业。
    """
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有职业列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的职业。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个职业",
    responses={200: ClassesSerializer()}
)
class ClassesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    职业获取、更新、删除视图，用于获取、更新或删除单个职业。
    """
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个职业。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个职业。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个职业。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="列出所有特性并创建新的特性",
    responses={200: TraitsSerializer(many=True)}
)
class TraitsListCreate(generics.ListCreateAPIView):
    """
    特性列表创建视图，用于获取所有特性列表或创建新的特性。
    """
    queryset = Traits.objects.all()
    serializer_class = TraitsSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有特性列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的特性。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个特性",
    responses={200: TraitsSerializer()}
)
class TraitsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    特性获取、更新、删除视图，用于获取、更新或删除单个特性。
    """
    queryset = Traits.objects.all()
    serializer_class = TraitsSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个特性。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个特性。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个特性。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="列出所有职业等级特性并创建新的职业等级特性",
    responses={200: ClassLevelFeaturesSerializer(many=True)}
)
class ClassLevelFeaturesListCreate(generics.ListCreateAPIView):
    """
    职业等级特性列表创建视图，用于获取所有职业等级特性列表或创建新的职业等级特性。
    """
    queryset = ClassLevelFeatures.objects.all()
    serializer_class = ClassLevelFeaturesSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有职业等级特性列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的职业等级特性。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个职业等级特性",
    responses={200: ClassLevelFeaturesSerializer()}
)
class ClassLevelFeaturesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    职业等级特性获取、更新、删除视图，用于获取、更新或删除单个职业等级特性。
    """
    queryset = ClassLevelFeatures.objects.all()
    serializer_class = ClassLevelFeaturesSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个职业等级特性。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个职业等级特性。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个职业等级特性。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="列出所有角色特性并创建新的角色特性",
    responses={200: CharacterTraitsSerializer(many=True)}
)
class CharacterTraitsListCreate(generics.ListCreateAPIView):
    """
    角色特性列表创建视图，用于获取所有角色特性列表或创建新的角色特性。
    """
    queryset = CharacterTraits.objects.all()
    serializer_class = CharacterTraitsSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有角色特性列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的角色特性。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个角色特性",
    responses={200: CharacterTraitsSerializer()}
)
class CharacterTraitsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    角色特性获取、更新、删除视图，用于获取、更新或删除单个角色特性。
    """
    queryset = CharacterTraits.objects.all()
    serializer_class = CharacterTraitsSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个角色特性。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个角色特性。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个角色特性。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="列出所有角色并创建新的角色",
    responses={200: CharactersSerializer(many=True)}
)
class CharactersListCreate(generics.ListCreateAPIView):
    """
    角色列表创建视图，用于获取所有角色列表或创建新的角色。
    """
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer

    def list(self, request, *args, **kwargs):
        """
        获取所有角色列表。
        """
        response = super().list(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def create(self, request, *args, **kwargs):
        """
        创建新的角色。
        """
        response = super().create(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)


@extend_schema(
    description="获取、更新或删除单个角色",
    responses={200: CharactersSerializer()}
)
class CharactersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    角色获取、更新、删除视图，用于获取、更新或删除单个角色。
    """
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        获取单个角色。
        """
        response = super().retrieve(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def update(self, request, *args, **kwargs):
        """
        更新单个角色。
        """
        response = super().update(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

    def destroy(self, request, *args, **kwargs):
        """
        删除单个角色。
        """
        response = super().destroy(request, *args, **kwargs)
        return CommonResponse.success(data=response.data)

