from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, permissions
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer

# Ingredients CRUD
class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]


# Recipes CRUD
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Ingredient.objects.filter(created_by=self.request.user)



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Recipe.objects.filter(created_by=self.request.user)


class RecipeSuggestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get ingredients from request
        user_ingredients = request.data.get("ingredients", [])
        if not user_ingredients:
            return Response({"error": "Please provide a list of ingredients."}, status=400)

        suggestions = []

        for recipe in Recipe.objects.all():
            recipe_ingredients = [i.name.lower() for i in recipe.ingredients.all()]
            user_ingredients_lower = [u.lower() for u in user_ingredients]

            # Count matches
            matches = [i for i in user_ingredients_lower if i in recipe_ingredients]
            match_percent = (len(matches) / len(recipe_ingredients)) * 100 if recipe_ingredients else 0
            missing_ingredients = [i for i in recipe_ingredients if i not in user_ingredients_lower]

            suggestions.append({
                "recipe": recipe.name,
                "match_percent": round(match_percent, 2),
                "missing_ingredients": missing_ingredients,
            })

        # Sort by match percent
        suggestions.sort(key=lambda x: x["match_percent"], reverse=True)

        return Response(suggestions)
