# from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet as Gen
from .serializers import RecipeSerializer
from .models import Recipe


class RecipesViewSet(Gen):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list_recipes(self, req: Request):
        pass

    def create_recipe(self, req: Request):
        pass

    def get_recipe(self, req: Request, recipe_id: int):
        pass

    def update_recipe(self, req: Request, recipe_id: int):
        pass

    def delete_recipe(self, req: Request, recipe_id: int):
        pass
