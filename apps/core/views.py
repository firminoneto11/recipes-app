from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet as Gen
from .serializers import RecipeSerializer
from .models import Recipe


class RecipesViewSet(Gen):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create_recipe(self, req: Request):
        serialized_object: RecipeSerializer = self.get_serializer(data=req.data)
        serialized_object.is_valid(raise_exception=True)
        serialized_object.save()
        return Response(data=serialized_object.data, status=201)

    def list_recipes(self, req: Request):
        serialized_data = self.get_serializer(instance=self.get_queryset(), many=True).data
        return Response(data=serialized_data, status=200)

    def get_recipe(self, req: Request, recipe_id: int):
        pass

    def update_recipe(self, req: Request, recipe_id: int):
        pass

    def delete_recipe(self, req: Request, recipe_id: int):
        pass
