from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet as Gen
from .serializers import RecipeSerializer
from .models import Recipe


class RecipesViewSet(Gen):

    queryset = Recipe.objects.all().order_by("-updated_at")
    serializer_class = RecipeSerializer

    def create_recipe(self, req: Request):
        """This view creates a new Recipe into the database with the data given in req.data"""
        serialized_object: RecipeSerializer = self.get_serializer(data=req.data)
        serialized_object.is_valid(raise_exception=True)
        serialized_object.save()
        return Response(data=serialized_object.data, status=201)

    def list_recipes(self, _req: Request):
        """This view return all the recipes in the database in a list"""
        serialized_data = self.get_serializer(instance=self.get_queryset(), many=True).data
        return Response(data=serialized_data)

    def get_recipe(self, _req: Request, recipe_id: int):
        """This view returns a single Recipe from the database based on the id informed on the route param"""
        recipe = get_object_or_404(Recipe, id=recipe_id)
        serialized_recipe_data = self.get_serializer(instance=recipe).data
        return Response(data=serialized_recipe_data)

    def update_recipe(self, req: Request, recipe_id: int):
        """
        This view updates a single Recipe based on the id informed on the route param. In the req.data the 'key' prop must be set and it
        should be the same as the 'key' property of the Recipe that is going to be updated. This way we make sure that only the person
        who created the Recipe can edit it
        """
        recipe: Recipe = get_object_or_404(Recipe, id=recipe_id)

        if "key" not in req.data.keys():
            return Response(data={"detail": "The Recipe's key must be set"}, status=400)
        if req.data["key"] != recipe.key:
            return Response(data={"detail": "The Recipe's key is invalid"}, status=400)

        serialized_recipe: RecipeSerializer = self.get_serializer(instance=recipe, data=req.data, partial=True)
        serialized_recipe.is_valid(raise_exception=True)
        serialized_recipe.save()
        return Response(data=serialized_recipe.data)

    def delete_recipe(self, _req: Request, recipe_id: int):
        """
        This view deletes a single Recipe from the database based on the id informed on the route param.
        """
        recipe: Recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return Response(status=204)
