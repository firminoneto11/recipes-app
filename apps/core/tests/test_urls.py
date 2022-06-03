from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import RecipesViewSet


class TestUrls(SimpleTestCase):
    def get_assertion_data(self, url: str, view: object, view_args: dict | None = None):
        view_name = resolve(url).func.__name__
        target_name = view.as_view(view_args).__name__
        msg = f"The view's name '{view_name}' should be equal to '{target_name}'"
        return view_name, target_name, msg

    def test_recipes(self):
        url = reverse("core:recipes")
        view_args = {"get": "list_recipes"}
        view_name, target_name, msg = self.get_assertion_data(url=url, view=RecipesViewSet, view_args=view_args)
        self.assertEqual(view_name, target_name, msg)

    def test_manage_recipe(self):
        url = reverse("core:manage-recipe", kwargs={"recipe_id": 1})
        view_args = {"get": "list_recipes"}
        view_name, target_name, msg = self.get_assertion_data(url=url, view=RecipesViewSet, view_args=view_args)
        self.assertEqual(view_name, target_name, msg)
