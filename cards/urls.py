from django.urls import path
from .views import *

urlpatterns = [
    # 规则系统
    path('rulesystems/', RuleSystemListCreate.as_view()),
    path('rulesystems/<int:pk>/', RuleSystemRetrieveUpdateDestroy.as_view()),
    
    # 角色管理
    path('characters/', CharactersListCreate.as_view()),
    path('characters/<int:pk>/', CharactersRetrieveUpdateDestroy.as_view()),
    
    # 规则系统
    path('rulesystems/', RuleSystemListCreate.as_view()),
    path('rulesystems/<int:pk>/', RuleSystemRetrieveUpdateDestroy.as_view()),
    
    # 属性管理
    path('attributes/', AttributesListCreate.as_view()),
    path('attributes/<int:pk>/', AttributesRetrieveUpdateDestroy.as_view()),
    
    # 职业管理
    path('classes/', ClassesListCreate.as_view()),
    path('classes/<int:pk>/', ClassesRetrieveUpdateDestroy.as_view()),
    
    # 特性管理
    path('traits/', TraitsListCreate.as_view()),
    path('traits/<int:pk>/', TraitsRetrieveUpdateDestroy.as_view()),
    
    # 职业等级特性
    path('classfeatures/', ClassLevelFeaturesListCreate.as_view()),
    path('classfeatures/<int:pk>/', ClassLevelFeaturesRetrieveUpdateDestroy.as_view()),
    
    # 角色特性
    path('charactertraits/', CharacterTraitsListCreate.as_view()),
    path('charactertraits/<int:pk>/', CharacterTraitsRetrieveUpdateDestroy.as_view())
]