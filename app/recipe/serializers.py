"""
Serializers for recipe app
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for recipe object. """

    # with this method we can call user.name (user objects have name attribute)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'description',
                  'time_minutes', 'price', 'link']
        read_only_fields = ['id']

    # here we are returning the name of the user object
    def get_user(self, obj):
        return obj.user.name


class RecipeDetailSerializer(RecipeSerializer):
    """ Serializer for recipe detail. """
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
