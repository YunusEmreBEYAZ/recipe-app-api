"""
Serializers for recipe app
"""
from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tags."""
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe object."""

    # with this method we can call user.name (user objects have name attribute)
    user = serializers.SerializerMethodField()
    # tags is a related field so we need to use a serializer for it
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'description',
                  'time_minutes', 'price', 'link', 'tags']
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
        """Helper method to get or create tags."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        return recipe

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    # here we are returning the name of the user object
    def get_user(self, obj):
        return obj.user.name


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail."""

    tags = TagSerializer(many=True, required=False)

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
