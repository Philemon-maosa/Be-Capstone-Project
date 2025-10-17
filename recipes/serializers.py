from rest_framework import serializers
from .models import Ingredient, Recipe

# Ingredient Serializer
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

# Recipe Serializer
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'quantity', 'instructions', 'ingredients', 'owner']
        read_only_fields = ['owner']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        user = self.context['request'].user  # the logged-in user

        # Create the recipe for the current user
        recipe = Recipe.objects.create(owner=user, **validated_data)

        # Create or get each ingredient — ensure owner is included
        for ing in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(
                name=ing['name'],
                owner=user   # ✅ include owner to avoid IntegrityError
            )
            recipe.ingredients.add(ingredient)

        return recipe
