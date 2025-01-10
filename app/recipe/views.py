"""
Views for the recipe app
"""

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing recipes in the database
    """
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """
        Return objects for the current authenticated user only
        """
        return self.queryset.filter(user=self.request.user).order_by('-id')

class PublicRecipeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for listing all recipes without authentication
    """
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


    def get_queryset(self):
        """
        Return all recipes ordered by newest first
        """
        print(self.permission_classes)
        print(self.authentication_classes)
        return self.queryset.order_by('-id')