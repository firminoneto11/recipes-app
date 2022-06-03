# from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet as Gen


class RecipesViewSet(Gen):
    def list_recipes(self, req: Request):
        pass

    def create_recipe(self, req: Request):
        pass

    def get_recipe(self, req: Request, recipe_id: int):
        pass

    def update_recipe(self, recipe_id: int):
        pass

    def delete_recipe(self, req: Request, recipe_id: int):
        pass
