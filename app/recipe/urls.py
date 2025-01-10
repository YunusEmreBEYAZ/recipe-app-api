"""
URLs for recipe app
"""

from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('', views.RecipeViewSet)
router.register('public-recipes', views.PublicRecipeViewSet, basename='public-recipes')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]