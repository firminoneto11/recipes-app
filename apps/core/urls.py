from django.urls import path
from .views import RecipesViewSet


app_name = "core"

urlpatterns = [
    path(
        route="recipes/",
        view=RecipesViewSet.as_view({"get": "list_recipes", "post": "create_recipe"}),
        name="recipes",
    ),
    path(
        route="recipe/<int:recipe_id>/",
        view=RecipesViewSet.as_view(
            {"get": "get_recipe", "put": "update_recipe", "patch": "update_recipe", "delete": "delete_recipe"}
        ),
        name="manage-recipe",
    ),
]
